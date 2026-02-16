import pygame
import random


pygame.mixer.pre_init(22050, -16, 2, 512)  # Lower frequency for faster processing
pygame.init()
pygame.font.init()


pygame.display.set_caption('PONG BY RYAN SATUR')



# Measurements
screen_width = 800
screen_height = 600

white = (255, 255, 255)
black = (0, 0, 0)

paddle_width = 15
paddle_height = 100

ball_size = 15


screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(r"fonts\Silkscreen-Regular.ttf", 74)
start_font = pygame.font.Font(r"fonts\Silkscreen-Regular.ttf", 30)

hit_sound = pygame.mixer.Sound(r"sfx\hit.wav")
score_sound = pygame.mixer.Sound(r"sfx\score.mp3")
bob = pygame.mixer.Sound(r"sfx\bob.wav")
icon_image = pygame.image.load(r"img\table-tennis-racket.ico")
pygame.display.set_icon(icon_image)
restart_icon = pygame.image.load("img/restart.png").convert_alpha()
pause_icon = pygame.image.load("img/pause.png").convert_alpha()
help_icon = pygame.image.load("img/questionmark.png").convert_alpha()

icon_size = 40
restart_icon = pygame.transform.scale(restart_icon, (icon_size, icon_size))
pause_icon = pygame.transform.scale(pause_icon, (icon_size, icon_size))
help_icon = pygame.transform.scale(help_icon, (icon_size, icon_size))


class Paddle:
    def __init__(self, x, y):
        
        self.rect = pygame.Rect(x, y, paddle_width, paddle_height)
        self.speed = 6

    def move(self, up=True):
        
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

class Ball:
    
    def __init__(self, x, y, speed=20):
        
        self.rect = pygame.Rect(x, y, ball_size, ball_size)
        self.speed_x = speed * random.choice((1, -1))
        self.speed_y = speed * random.choice((1, -1))
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            hit_sound.play()
            self.speed_y *= -1

    def draw(self):
        if self.rect:
            pygame.draw.ellipse(screen, white, self.rect)

    def hide(self):
        self.rect = None

def start_screen():
    screen.fill(black)

    title_text = font.render("PONG", True, white)
    option_font = pygame.font.Font(r"fonts\Silkscreen-Regular.ttf", 28)

    slow_text = option_font.render("1 - Slow", True, white)
    normal_text = option_font.render("2 - Normal", True, white)
    fast_text = option_font.render("3 - Fast", True, white)

    screen.blit(title_text,
                (screen_width // 2 - title_text.get_width() // 2, 120))
    screen.blit(slow_text,
                (screen_width // 2 - slow_text.get_width() // 2, 260))
    screen.blit(normal_text,
                (screen_width // 2 - normal_text.get_width() // 2, 310))
    screen.blit(fast_text,
                (screen_width // 2 - fast_text.get_width() // 2, 360))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 4.8
                if event.key == pygame.K_2:
                    return 5.8
                if event.key == pygame.K_3:
                    return 6.8

def choose_speed():
    screen.fill(black)

    title_text = font.render("Choose Speed", True, white)
    option_font = pygame.font.Font(r"fonts\Silkscreen-Regular.ttf", 28)

    slow_text = option_font.render("1 - Slow", True, white)
    normal_text = option_font.render("2 - Normal", True, white)
    fast_text = option_font.render("3 - Fast", True, white)

    screen.blit(title_text,
                (screen_width // 2 - title_text.get_width() // 2, 150))
    screen.blit(slow_text,
                (screen_width // 2 - slow_text.get_width() // 2, 280))
    screen.blit(normal_text,
                (screen_width // 2 - normal_text.get_width() // 2, 330))
    screen.blit(fast_text,
                (screen_width // 2 - fast_text.get_width() // 2, 380))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 4.8      # Slow speed
                if event.key == pygame.K_2:
                    return 5.8      # Normal speed
                if event.key == pygame.K_3:
                    return 6.8      # Fast speed


def countdown(message=""):
    clock = pygame.time.Clock()

    for i in range(3, 0, -1):
        start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start_time < 1000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        pygame.quit()
                        exit()

            screen.fill(black)

            if message:
                msg_text = start_font.render(message, True, white)
                screen.blit(
                    msg_text,
                    (
                        screen_width // 2 - msg_text.get_width() // 2,
                        screen_height // 2 - 100
                    )
                )

            number_text = font.render(str(i), True, white)
            screen.blit(
                number_text,
                (
                    screen_width // 2 - number_text.get_width() // 2,
                    screen_height // 2 - number_text.get_height() // 2
                )
            )

            pygame.display.flip()
            clock.tick(60)

def show_help():
    showing = True
    help_font = pygame.font.Font(r"fonts\Silkscreen-Regular.ttf", 22)

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    showing = False

        screen.fill(black)

        lines = [
            "Controls:",
            "Player 1: W / S",
            "Player 2: UP ARROW / DOWN ARROW",
            "Pause: Press button or press P",
            "Restart: Press button or press M",
            "ESC - Quit",
            "",
            "Press ESC to Close Help"
        ]

        for i, line in enumerate(lines):
            text = help_font.render(line, True, white)
            screen.blit(
                text,
                (
                    screen_width // 2 - text.get_width() // 2,
                    120 + i * 40
                )
            )

        pygame.display.flip()


def game_loop(initial_ball_speed=5.3):
    clock = pygame.time.Clock()
    running = True

    player_start_x = screen_width - 20
    player_start_y = screen_height // 2 - paddle_height // 2
    opponent_start_x = 10
    opponent_start_y = screen_height // 2 - paddle_height // 2

    player = Paddle(player_start_x, player_start_y)
    opponent = Paddle(opponent_start_x, opponent_start_y)

    # --- NEW SYSTEM VARIABLES ---
    restart_button = restart_icon.get_rect(topleft=(screen_width//2 - 60, 20))
    pause_button = pause_icon.get_rect(topleft=(screen_width//2 - 20, 20))
    help_button = help_icon.get_rect(topleft=(screen_width//2 + 20, 20))

    paused = False
    # ----------------------------

    ball = Ball(
        screen_width // 2 - ball_size // 2,
        screen_height // 2 - ball_size // 2,
        speed=initial_ball_speed
    )

    player_score = 0
    opponent_score = 0
    winning_score = 11

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

                # Pause toggle
                if event.key == pygame.K_p:
                    paused = not paused
            
            if (event.type == pygame.MOUSEBUTTONDOWN and restart_button.collidepoint(event.pos)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_m):
                return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pause_button.collidepoint(event.pos):
                    paused = not paused

                if help_button.collidepoint(event.pos):
                    paused = True
                    show_help()


        keys = pygame.key.get_pressed()

        if not paused:
            if keys[pygame.K_UP] and player.rect.top > 0:
                player.move(up=True)
            if keys[pygame.K_DOWN] and player.rect.bottom < screen_height:
                player.move(up=False)
            if keys[pygame.K_w] and opponent.rect.top > 0:
                opponent.move(up=True)
            if keys[pygame.K_s] and opponent.rect.bottom < screen_height:
                opponent.move(up=False)

            ball.move()

        # Ball collisions with paddles
        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(opponent.rect):
            hit_sound.play()
            if ball.rect.colliderect(player.rect):
                ball.rect.right = player.rect.left
            else:
                ball.rect.left = opponent.rect.right
            ball.speed_x *= -1

        # Scoring
        if ball.rect.left <= 0:
            player_score += 1
            score_sound.play()

            
            if player_score == winning_score:
                bob.play()
                display_winner("Player 1 Wins!", initial_ball_speed)
                running = False
                continue

            countdown("Next Round")

            ball = Ball(
                screen_width // 2 - ball_size // 2,
                screen_height // 2 - ball_size // 2,
                speed=initial_ball_speed
            )

            player.rect.y = player_start_y
            opponent.rect.y = opponent_start_y

        if ball.rect.right >= screen_width:
            opponent_score += 1
            score_sound.play()

            if opponent_score == winning_score:
                bob.play()
                display_winner("Player 2 Wins!", initial_ball_speed)
                running = False
                continue

            countdown("Next Round")

            ball = Ball(
                screen_width // 2 - ball_size // 2,
                screen_height // 2 - ball_size // 2,
                speed=initial_ball_speed
            )

            player.rect.y = player_start_y
            opponent.rect.y = opponent_start_y

        # Drawing
        screen.fill(black)

        player.draw()
        opponent.draw()
        ball.draw()

        screen.blit(restart_icon, restart_button)
        screen.blit(pause_icon, pause_button)
        screen.blit(help_icon, help_button)

        player_text = font.render(str(player_score), True, white)
        opponent_text = font.render(str(opponent_score), True, white)

        screen.blit(player_text, (screen_width - 100, 10))
        screen.blit(opponent_text, (50, 10))



        # Paused overlay
        if paused:
            overlay = font.render("PAUSED", True, white)
            screen.blit(
                overlay,
                (
                    screen_width // 2 - overlay.get_width() // 2,
                    screen_height // 2 - overlay.get_height() // 2
                )
            )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def display_winner(winner_text, ball_speed):
    screen.fill(black)
    text = font.render(winner_text, True, white)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    option_font = pygame.font.Font(r"fonts\Silkscreen-Regular.ttf", 20)
    play_again_text = option_font.render("Press R to Play Again or Q to Quit", True, white)
    screen.blit(play_again_text, (screen_width // 2 - play_again_text.get_width() // 2, screen_height // 2 + 50))
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    bob.stop()
                    chosen_speed = start_screen()
                    countdown("Get Ready")
                    game_loop(chosen_speed)
                    waiting_for_input = False
                elif event.key == pygame.K_q:
                    bob.stop()
                    waiting_for_input = False

if __name__ == "__main__":
    running = True
    while running:
        chosen_speed = start_screen()
        countdown("Get Ready")
        result = game_loop(chosen_speed)

        if result == "quit":
            running = False


