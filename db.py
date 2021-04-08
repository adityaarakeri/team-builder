from tinydb import TinyDB, Query

class Player_DB:

    def __init__(self):
        self.db = TinyDB('db.json')
        self.player = Query()

    def insert(self, player_dict):
        """
        takes a player_dict of format
        { 
            name: player-name
            current_eff : current-efficacy
            previous_eff: previous-efficacy
        }
        """
        self.db.insert(player_dict)

    def all(self):
        """
        return all items
        """
        return self.db.all()

    def search(self, name):
        """search a player efficacy by name
        """
        return self.db.search(self.player.name == name)

    def update(self, name, new_efficacy):
        """search a player using his name and update his efficacy
        """

        self.db.update(
            { 'efficacy': new_efficacy }, 
            self.player.name == name
            )

    def truncate(self):
        """
        use it wisely clears out the entire db
        """
        self.db.truncate()
