import math
import time
import random
import pygame

# Screen Resolution and Setup Constants
RESOLUTION = (2560, 1440)
WIDTH, HEIGHT = RESOLUTION
FPS = 165
FULLSCREEN = True
APP_VERSION = "1.0"
APP_NAME = "My App"
ICON_LOCATION = ""

# Print app name and version at the start
print(f"{APP_NAME} {APP_VERSION}")

# PyGame Setup
pygame.init()
SCREEN = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN if FULLSCREEN else 0)
pygame.display.set_caption(APP_NAME)
# pygame.display.set_icon(pygame.image.load(ICON_LOCATION))  # Uncomment if an icon is present

clock = pygame.time.Clock()
delta_time = 0.0
font = pygame.font.SysFont("Arial", 32)


def timer(func):
    """
    Timer decorator to measure execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {(end - start) * 1000:.2f} ms to execute.")
        return output

    return wrapper


def clamp(value, min_value, max_value):
    """
    Clamps the value between the minimum and maximum values.
    """
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    """
    Linear interpolation between start and end with a factor of t.
    """
    return start + t * (end - start)


def map_value(value, start1, stop1, start2, stop2):
    """
    Maps a value from one range to another.
    """
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


def manage_frame_rate(clock, get_ticks_last_frame):
    """
    Manages frame rate and calculates delta time.
    """
    clock.tick(FPS)
    t = pygame.time.get_ticks()
    delta_time = (t - get_ticks_last_frame) / 1000.0
    return t, delta_time


def draw_circle(screen, color, position, radius):
    """
    Draws a circle on the screen.
    """
    pygame.draw.circle(screen, color.get_tup(), (int(position.x), int(position.y)), radius)


def draw_rectangle(screen, color, position, size):
    """
    Draws a rectangle on the screen.
    """
    pygame.draw.rect(screen, color.get_tup(), pygame.Rect(position.x, position.y, size.x, size.y))


def draw_line(screen, color, start_pos, end_pos, width=1):
    """
    Draws a line between two points on the screen.
    """
    pygame.draw.line(
        screen,
        color.get_tup(),
        (int(start_pos.x), int(start_pos.y)),
        (int(end_pos.x), int(end_pos.y)),
        width,
    )


def distance_between_points(p1, p2):
    """
    Calculates the Euclidean distance between two points.
    """
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def random_float(min_value=0.0, max_value=1.0):
    """
    Generates a random float between a specified range.
    """
    return random.uniform(min_value, max_value)


def sign(value):
    """
    Returns the sign of a value (-1 for negative, 1 for positive, 0 for zero).
    """
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


class Color:
    def __init__(self, r=255, g=255, b=255):
        self.r, self.g, self.b = r, g, b

    def init_colors(self):
        self.BLACK = Color(0, 0, 0)
        self.DARK_GRAY = Color(85, 85, 85)
        self.LIGHT_GRAY = Color(170, 170, 170)
        self.WHITE = Color(255, 255, 255)
        self.RED = Color(255, 0, 0)
        self.LIME = Color(0, 255, 0)
        self.BLUE = Color(0, 0, 255)
        self.YELLOW = Color(255, 255, 0)
        self.PINK = Color(255, 0, 255)
        self.LIGHT_BLUE = Color(0, 255, 255)
        self.GREEN = Color(0, 128, 0)
        self.PURPLE = Color(128, 0, 128)
        self.DARK_BLUE = Color(0, 0, 128)
        self.ORANGE = Color(255, 170, 0)
        self.BROWN = Color(128, 60, 0)

    @staticmethod
    def random():
        """
        Returns a random color.
        """
        return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def blend(self, other, ratio=0.5):
        """
        Blends two colors based on a ratio.
        """
        r = int(self.r * ratio + other.r * (1 - ratio))
        g = int(self.g * ratio + other.g * (1 - ratio))
        b = int(self.b * ratio + other.b * (1 - ratio))
        return Color(r, g, b)

    def to_hex(self, prefix="#"):
        """
        Converts color to hexadecimal string.
        """
        return f"{prefix}{self.r:02x}{self.g:02x}{self.b:02x}"

    def to_hsl(self, hue_angle=True):
        """
        Converts RGB to HSL (Hue, Saturation, Lightness).
        """
        r, g, b = self.r / 255, self.g / 255, self.b / 255
        max_color = max(r, g, b)
        min_color = min(r, g, b)
        l = (max_color + min_color) / 2

        if max_color == min_color:
            h = s = 0
        else:
            diff = max_color - min_color
            s = diff / (2 - max_color - min_color) if l > 0.5 else diff / (max_color + min_color)
            if max_color == r:
                h = (g - b) / diff + (6 if g < b else 0)
            elif max_color == g:
                h = (b - r) / diff + 2
            else:
                h = (r - g) / diff + 4
            h /= 6

        return (h * 360 if hue_angle else h, s, l)

    def get_tup(self):
        """
        Returns the color as a tuple (r, g, b).
        """
        return self.r, self.g, self.b

    def __repr__(self) -> str:
        return f"R: {self.r}, G: {self.g}, B: {self.b}"


# Colors Setup
colors = Color()
colors.init_colors()


class Vector2:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def init_vectors(self):
        self.ZERO = Vector2(0, 0)
        self.ONE = Vector2(1, 1)
        self.NEG_ONE = Vector2(-1, -1)
        self.RIGHT = Vector2(1, 0)
        self.LEFT = Vector2(-1, 0)
        self.UP = Vector2(0, 1)
        self.DOWN = Vector2(0, -1)

    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        """
        Normalizes the vector (sets its length to 1).
        """
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)

    def dot(self, other):
        """
        Calculates the dot product of two vectors.
        """
        return self.x * other.x + self.y * other.y

    def angle_between(self, other):
        """
        Calculates the angle between two vectors in radians.
        """
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def rotate(self, angle):
        """
        Rotates the vector by a given angle in degrees.
        """
        rad = math.radians(angle)
        cos_theta, sin_theta = math.cos(rad), math.sin(rad)
        return Vector2(
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta,
        )

    def scale(self, factor):
        """
        Scales the vector by a factor.
        """
        return Vector2(self.x * factor, self.y * factor)

    def translate(self, dx, dy):
        """
        Translates the vector by dx and dy.
        """
        return Vector2(self.x + dx, self.y + dy)

    def get_tup(self):
        """
        Returns the vector as a tuple (x, y).
        """
        return self.x, self.y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        raise TypeError(f"Unsupported operand type(s) for *: 'Vector2' and '{type(other)}'")

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        raise TypeError(f"Unsupported operand type(s) for /: 'Vector2' and '{type(other)}'")

    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def init_vectors(self):
        self.ZERO = Vector3(0, 0, 0)
        self.ONE = Vector3(1, 1, 0)
        self.NEG_ONE = Vector3(-1, -1, 0)
        self.RIGHT = Vector3(1, 0, 0)
        self.LEFT = Vector3(-1, 0, 0)
        self.UP = Vector3(0, 1, 0)
        self.DOWN = Vector3(0, -1, 0)
        self.FORWARD = Vector3(0, 0, 1)
        self.BACK = Vector3(0, 0, -1)

    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2, self.z**2)

    def normalize(self):
        """
        Normalizes the vector (sets its length to 1).
        """
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other):
        """
        Calculates the dot product of two vectors.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle_between(self, other):
        """
        Calculates the angle between two vectors in radians.
        """
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def scale(self, factor):
        """
        Scales the vector by a factor.
        """
        return Vector3(self.x * factor, self.y * factor, self.z * factor)

    def translate(self, dx, dy, dz):
        """
        Translates the vector by dx, dy and dz.
        """
        return Vector3(self.x + dx, self.y + dy, self.z + dz)

    def get_tup(self):
        """
        Returns the vector as a tuple (x, y, z).
        """
        return self.x, self.y, self.z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError(f"Unsupported operand type(s) for *: 'Vector3' and '{type(other)}'")

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x / other, self.y / other, self.z / other)
        raise TypeError(f"Unsupported operand type(s) for /: 'Vector3' and '{type(other)}'")

    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}, Z: {self.z}"


# Vector2 and Vector3 Setup
vector2 = Vector2()
vector2.init_vectors()

vector3 = Vector3()
vector3.init_vectors()


class Rect:
    def __init__(self, position: Vector2, scale: Vector2):
        self.position = position
        self.scale = scale

    def get_pg_rect(self):
        return (
            self.position.x - self.scale.x // 2,
            self.position.y - self.scale.y // 2,
            self.scale.x,
            self.scale.y,
        )


class Circle:
    def __init__(self, position: Vector2, radius: int):
        self.position = position
        self.radius = radius


class Grid:
    def __init__(self, x, y, default_bg_color):
        self.x, self.y = x, y
        self.grid = [[default_bg_color for _ in range(y)] for _ in range(x)]

        self.cell_width = WIDTH / self.x
        self.cell_height = HEIGHT / self.y

        self.total_width = self.cell_width * self.x
        self.total_height = self.cell_height * self.y

        self.offset_x = (WIDTH - self.total_width) // 2
        self.offset_y = (HEIGHT - self.total_height) // 2

    def set_square(self, position, color):
        self.grid[position.x][position.y] = color

    def draw(self, surface: pygame.Surface, color: Color, border_width: int):
        for x in range(self.x):
            for y in range(self.y):
                rect = pygame.Rect(
                    self.offset_x + x * self.cell_width,
                    self.offset_y + y * self.cell_height,
                    self.cell_width,
                    self.cell_height,
                )

                pygame.draw.rect(surface, self.grid[x][y].get_tup(), rect)
                pygame.draw.rect(surface, color.get_tup(), rect, border_width)


def rect_collision(rect1: Rect, rect2: Rect):
    return pygame.Rect.colliderect(rect1.get_pg_rect(), rect2.get_pg_rect())


def circle_collsion(circle1: Circle, circle2: Circle):
    dst = circle1.position - circle2.position
    dst = dst.magnitude()

    if dst > circle1.radius + circle2.radius:
        return False

    return True


def run(start, update):
    running = True

    # Run the start function the first frame
    start()

    while running:
        # Run the update function every frame
        running = update()
