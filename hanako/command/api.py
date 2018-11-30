class WorldStateAPI:
    """Programmable API for managing the World State.
    """

    def get_world(self, world_id, at_hash):
        """Fetch as :class:`hanako.model.World` by its ``id`` and at given ``hash`` version.
        """
        pass

    def get_actions(self, world_id, after_hash):
        """Returns a list of :class:`hanako.model.Action` for a given ``World`` **after**
        the provided version ``hash``.
        """
        pass
    
    def execute_action(self, world_id, action):
        """Executes the given :class:`hanako.model.Action` for the world with ``world_id``.
        """
        pass