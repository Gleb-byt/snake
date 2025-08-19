import pygame
from .constants import *
from .direction import Directions
from .element import Element

class Infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE,HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None,SCALE)
        
    def is_quit_event(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def get_pressed_key(self) -> Directions | None:
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            return Directions.DOWN
        elif key[pygame.K_s]:
            return Directions.UP
        elif key[pygame.K_d]:
            return Directions.RIGHT
        elif key[pygame.K_a]:
            return Directions.LEFT
        return None
    
    def fill_screen(self) -> None:
        self.screen.fill(SCREEN_COLOR)
        
    def draw_element(self,e:Element,color) -> None:
        pygame.draw.rect(
            self.screen,
            pygame.Color(color),
            (e.x *SCALE, e.y * SCALE, ELEMENT_SIZE,ELEMENT_SIZE),
            0,
            ELEMENT_RADIUS
        )
        
    def draw_score(self,score : int) -> None:
        self.screen.blit(
            self.font.render(f"Score: {score}",True,pygame.Color(SCORE_COLOR)),
            (5,5)
        )
        
    def draw_game_over(self) -> None:
        messege = self.font.render("GAME OVER",True,pygame.Color(SCORE_COLOR))
        self.screen.blit(
            messege,
            messege.get_rect(center = ((WIDTH // 2) *SCALE,(HEIGHT//2) * SCALE))
        )
        
    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)
        
    def quit(self) -> None:
        pygame.quit()