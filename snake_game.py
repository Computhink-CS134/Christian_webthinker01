"""
Snake Game - A classic pygame-based Snake game
Controls: Arrow keys to move, SPACE to pause, Q to quit
"""

import pygame
import sys
import random
from enum import Enum
from collections import deque


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class SnakeGame:
    # Game constants
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    GRID_SIZE = 20
    GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
    GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
    FPS = 10
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    DARK_GREEN = (0, 200, 0)
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)
        
        self.reset_game()
    
    def reset_game(self):
        """Initialize or reset game state"""
        # Snake starts in the middle
        start_x = self.GRID_WIDTH // 2
        start_y = self.GRID_HEIGHT // 2
        self.snake = deque([
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ])
        
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def spawn_food(self):
        """Spawn food at a random location not occupied by snake"""
        while True:
            x = random.randint(0, self.GRID_WIDTH - 1)
            y = random.randint(0, self.GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def handle_events(self):
        """Handle user input and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                    return True
                
                # Direction controls (prevent 180-degree turns)
                if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.next_direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.next_direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.next_direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.next_direction = Direction.RIGHT
        
        return True
    
    def update(self):
        """Update game state"""
        if self.game_over or self.paused:
            return
        
        # Update direction
        self.direction = self.next_direction
        
        # Move snake
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw(self):
        """Draw game elements"""
        self.screen.fill(self.BLACK)
        
        # Draw grid (optional)
        for x in range(0, self.WINDOW_WIDTH, self.GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, self.WINDOW_HEIGHT))
        for y in range(0, self.WINDOW_HEIGHT, self.GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (self.WINDOW_WIDTH, y))
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            rect = pygame.Rect(x * self.GRID_SIZE + 2, y * self.GRID_SIZE + 2,
                              self.GRID_SIZE - 4, self.GRID_SIZE - 4)
            # Head is brighter
            color = self.YELLOW if i == 0 else self.GREEN
            pygame.draw.rect(self.screen, color, rect)
        
        # Draw food
        food_x, food_y = self.food
        food_rect = pygame.Rect(food_x * self.GRID_SIZE + 2, food_y * self.GRID_SIZE + 2,
                               self.GRID_SIZE - 4, self.GRID_SIZE - 4)
        pygame.draw.rect(self.screen, self.RED, food_rect)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw pause message
        if self.paused:
            pause_text = self.font.render("PAUSED - Press SPACE to resume", True, self.YELLOW)
            text_rect = pause_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, text_rect)
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.large_font.render("GAME OVER", True, self.RED)
            score_text = self.font.render(f"Final Score: {self.score}", True, self.WHITE)
            restart_text = self.font.render("Press R to Restart or Q to Quit", True, self.WHITE)
            
            game_over_rect = game_over_text.get_rect(center=(self.WINDOW_WIDTH // 2, 
                                                             self.WINDOW_HEIGHT // 2 - 60))
            score_rect = score_text.get_rect(center=(self.WINDOW_WIDTH // 2, 
                                                    self.WINDOW_HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(self.WINDOW_WIDTH // 2, 
                                                        self.WINDOW_HEIGHT // 2 + 60))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
