from functools import reduce
from hashlib import sha256

__ACTIONS = {}

class WorldStateAPI:
    """Programmable API for managing the World State.
    """

    def __init__(self, world_repo, action_repo, bulk_size=1024):
        self.world_repo = world_repo
        self.action_repo = action_repo
        self.bulk_size = bulk_size

    def get_world(self, world_id, at_hash):
        """Fetch as :class:`hanako.model.World` by its ``id`` and at given ``hash`` version.
        """
        world = self.world_repo.get_by_hash(world_id, at_hash)
        if world is not None:
            return world
        return self._calculate_world_state(world_id, at_hash)


    def get_actions(self, world_id, after_hash, page, page_size):
        """Returns a list of :class:`hanako.model.Action` for a given ``World`` **after**
        the provided version ``hash``.
        """
        action = self.action_repo.get_by_hash(after_hash)

        return self.action_repo.get_all({
            "worldId": world_id,
            "hash": {
                "$gt": action.timestamp,
            }
        }, page, page_size)
    
    def execute_action(self, world_id, action):
        """Executes the given :class:`hanako.model.Action` for the world with ``world_id``.
        """
        world = self.world_repo.get_latest_state(world_id)

        next_hash = next_hash(world, fold_action(action))

        state_update = {
            "hash": next_hash,
            action.property: action.value,
        }

        self.world_repo.update_world(world_id, state_update)
        action.state_hash = world.state_hash

        self.action_repo.save(action)


    def _calculate_world_state(self, world_id, at_hash):
        state = self.world_repo.get_last_before(world_id, at_hash)

        while True:
            actions = self.action_repo.get_after(at_hash)
            if !actions:
                raise Exception("Cannot calculate world (%s) state at hash (%s)" %  (world_id, at_hash))
            
            (state, hash_reached) = reduce(lambda (action, reached): (apply_action(state, action) \
                            if action.state_hash !=at_hash else state, \
                            True if action.state_hash == at_hash else hash_reached), actions, (state, False))
            if hash_reached:
                break
        return state

def apply_action(state, action):
    actionfn = __ACTIONS.get(action.verb)
    if not actionfn:
        raise Exception('Invalid action: %s' % action.verb)
    return actionfn(state, action)


def set_action(state, action):
    prev = None
    if hasattr(state, action.property):
        prev = getattr(state, action.property)
    setattr(state, action.property, action.value)
    return state

def delete_action(state, action):
    prev = None
    if hasattr(state, action.property):
        prev = getattr(state, action.property)
    delattr(state, action.property)
    return state

# register the action methods
__ACTIONS.update({
    "set": set_action,
    "update": set_action,
    "delete": delete_action,
    "del": delete_action,
})

def next_hash(state, additional):
    if state.state_hash is not None:
        return __next_sha256(state.state_hash + additional)
    return __next_sha256(additional)

def __next_sha256(message):
    return sha256(message).hexdigest()

def fold_action(action):
    return action.type + (action.value or "")

