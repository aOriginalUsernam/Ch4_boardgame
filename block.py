import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int, img: pygame.image) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.rect: pygame.rect.Rect = pygame.Rect(x, y, size, size)
        self.rect.center = [x, y]
        self.image: pygame.Surface = pygame.transform.scale(img, (size, size))

    def copy(self, x: int, y: int):
        return Block(x, y, self.size, self.image)

    def move(self, entities: pygame.sprite.Group, dx: int = 0, dy: int = 0) -> tuple:
        # Move each axis separately. check for collision both times.
        to_return: list = []
        if dx != 0:
            to_return.append(self.__move_single_axis__(entities.sprites(), dx, 0))
        if dy != 0:
            to_return.append(self.__move_single_axis__(entities.sprites(), 0, dy))
        return tuple(to_return)

    def __move_single_axis__(
        self, entities: list, dx: int = 0, dy: int = 0
    ) -> pygame.sprite.Sprite | None:
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        to_return = None

        # If you collide with another entity, move out based on velocity
        for entity in entities:
            if self.rect.colliderect(entity.rect):
                to_return = entity
                if dx > 0:  # if Moving right; Hit the left side of the entity
                    self.rect.right = entity.rect.left
                if dx < 0:  # if Moving left; Hit the right side of the entity
                    self.rect.left = entity.rect.right
                if dy > 0:  # if Moving down; Hit the top side of the entity
                    self.rect.bottom = entity.rect.top
                if dy < 0:  # if Moving up; Hit the bottom side of the entity
                    self.rect.top = entity.rect.bottom
        return to_return
