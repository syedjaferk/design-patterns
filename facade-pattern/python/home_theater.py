# Subsystem classes
class Amplifier:
    def turn_on(self):
        """        Turn on the amplifier.

        Prints a message indicating that the amplifier has been turned on.
        """

        print("Amplifier turned on")

    def turn_off(self):
        """        Turn off the amplifier.

        This function turns off the amplifier and prints a message indicating that the amplifier has been turned off.
        """

        print("Amplifier turned off")


class DVDPlayer:
    def play_movie(self, movie):
        """        Play the specified movie.

        Args:
            movie (str): The name of the movie to be played.
        """

        print(f"Playing movie: {movie}")

    def stop_movie(self):
        """        Stop the currently playing movie.

        This method stops the currently playing movie.
        """

        print("Stopping movie")


class Projector:
    def turn_on(self):
        """        Turn on the projector.

        This function turns on the projector and prints a message indicating that the projector has been turned on.
        """

        print("Projector turned on")

    def turn_off(self):
        """        Turn off the projector.

        This method turns off the projector by performing the necessary actions.
        """

        print("Projector turned off")


class Lights:
    def dim_lights(self):
        """        Dim the lights.

        This function dims the lights in the room.
        """

        print("Dimming lights")

    def brighten_lights(self):
        """        Brighten the lights.

        This method brightens the lights in the environment.
        """

        print("Brightening lights")


# Facade class
class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, projector, lights):
        """        Initialize a new HomeTheater object with the provided components.

        Args:
            amplifier (str): The brand and model of the amplifier.
            dvd_player (str): The brand and model of the DVD player.
            projector (str): The brand and model of the projector.
            lights (str): The type of lighting system used in the home theater.
        """

        self.amplifier = amplifier
        self.dvd_player = dvd_player
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie):
        """        Get ready to watch a movie.

        This method prepares the home theater system to watch a movie by dimming the lights, turning on the amplifier,
        turning on the projector, and playing the specified movie.

        Args:
            movie (str): The name of the movie to be played.
        """

        print("Get ready to watch a movie!")
        self.lights.dim_lights()
        self.amplifier.turn_on()
        self.projector.turn_on()
        self.dvd_player.play_movie(movie)

    def end_movie(self):
        """        End the movie night and turn off all the equipment.

        This function prints a message indicating that the movie night is over and then proceeds to stop the DVD player,
        turn off the amplifier, projector, and brighten the lights.

        Args:
            self: The instance of the class.
        """

        print("Movie night is over!")
        self.dvd_player.stop_movie()
        self.amplifier.turn_off()
        self.projector.turn_off()
        self.lights.brighten_lights()


# Client code
amplifier = Amplifier()
dvd_player = DVDPlayer()
projector = Projector()
lights = Lights()

home_theater = HomeTheaterFacade(amplifier, dvd_player, projector, lights)

# Watching a movie using the Facade
home_theater.watch_movie("Inception")

# Ending the movie night
home_theater.end_movie()
