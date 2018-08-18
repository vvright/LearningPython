class Scene(object):
    def __init__(self):
        pass

    def enter(self):
        pass


class Death(Scene):
    def enter(self):
        pass


class CentralCorridor(Scene):
    def enter(self):
        pass


class LaserWeaponArmory(Scene):
    def enter(self):
        pass


class TheBridge(Scene):
    def enter(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass


class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene
        pass

    #   def __init__(self):
    #       pass


def next_scene(self, scene_name):
    pass


def opening_scene(self):
    pass


class Engine(object):
    def __init__(self, scene_map):
        pass

    #   def __init__(self, start_scene):
    #       super(Engine, self).__init__(start_scene)
    #       pass

    #   def __init__(self, start_scene, scene_map):
    #        super(Engine, self).__init__(start_scene)
    #       self.scene_map = scene_map
    #       pass

    def play(self):
        pass


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
