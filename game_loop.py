import os
import json
import pygame
from text import *
from shape import *
from shapeHandler import *
from shapes import *
from grid import *
from block import *
from board import *
from menu import *


with open("save_file1.json", "w") as file:
    pass


class GameLoop:
    def __init__(
        self,
        clock: pygame.time.Clock,
        screen: pygame.display,
        width_and_height: tuple[int, int] = [1000, 500],
        margin: int = 230,
        cell_amount: int = 10,
        cell_size: int = 50,
        load_game: bool = False,
    ) -> None:
        self.save_path = os.path.join(os.getcwd(), f"data\\save_file.json")

        if load_game:
            self.load_game(clock, screen)
        else:
            self.start_game(
                clock, screen, width_and_height, margin, cell_amount, cell_size
            )

    def start_game(
        self,
        clock: pygame.time.Clock,
        screen: pygame.display,
        width_and_height: tuple[int, int],
        margin: int,
        cell_amount: int,
        cell_size: int,
    ) -> bool:
        # set clock, names and grid
        self.clock = clock
        self.name_player1 = get_names(clock, screen, "Name player one")
        self.name_player2 = get_names(clock, screen, "Name player two")
        # self.margin = margin
        # self.cell_amount = cell_amount
        self.grid = Grid(cell_size, cell_amount, margin)

        # draw grid
        self.grid.draw_grid(screen)
        self.width_and_height = width_and_height
        width = width_and_height[0]
        height = width_and_height[1]
        # make timer
        font = pygame.font.Font(None, 36)
        timer = Timer(font, int(width / 2), 36 / 2, 15)
        self.timer = timer

        # points
        points = 0
        points_p1 = Points(font, points, 0.5 * margin, 50)
        points_p2 = Points(font, points, width - 0.5 * margin, 50)
        self.points = {"red": points_p1, "green": points_p2}

        # MAKE PLAYER BOARDs
        board_col = pygame.Color(10, 10, 10)
        p1_board = Board(board_col, 0, 0, margin, height)
        p2_board = Board(board_col, width - margin, 0, margin, height)
        self.boards = (p1_board, p2_board)

        # load images
        r_block_img = pygame.image.load(
            os.path.join(os.getcwd(), "images\\block_red.png")
        )
        g_block_img = pygame.image.load(
            os.path.join(os.getcwd(), "images\\block_green.png")
        )
        rotate_image = pygame.image.load(
            os.path.join(os.getcwd(), "images\\rotate.png")
        )
        rotate_img_model = Image(rotate_image, width / 2, 100, 80)
        self.rotate_img = rotate_img_model

        # make block + shape handler
        red_block = Block(
            self.grid.cell_size + 10,
            height - margin + self.grid.cell_size + 10,
            cell_size,
            r_block_img,
        )
        green_block = Block(
            width - margin + self.grid.cell_size + 10,
            height - margin + self.grid.cell_size + 10,
            cell_size,
            g_block_img,
        )
        self.shape_handler = ShapeHandler(
            {"red": red_block, "green": green_block}, int(margin - cell_size / 2)
        )

        # make current shape
        self.current_shape = self.shape_handler.generate_shape("red")
        self.current_shape.move(self.grid.cell_size, int(height / 2))

        # make next shapes
        p1_next_shape = self.shape_handler.generate_shape("red")

        p2_next_shape = self.shape_handler.generate_shape("green")
        self.next_shapes = {"red": p1_next_shape, "green": p2_next_shape}

        self.is_player_1 = True

    def load_game(
        self,
        clock: pygame.time.Clock,
        screen: pygame.display,
    ) -> bool:
        try:
            with open(self.save_path, "r") as file:
                file_dict = json.load(file)
                file_current_shape = file_dict["current_shape"]
                file_shapes = file_dict["shapes"]
                file_grid = file_dict["grid"]
                file_points = file_dict["points"]
        except:
            raise SystemExit("no valid safe_file")

        self.clock = clock
        self.width_and_height = file_dict["width_and_height"]
        width_and_height = self.width_and_height

        # set screen
        screen = screen = pygame.display.set_mode(
            (width_and_height[0], width_and_height[1])
        )

        # usefull data
        width = width_and_height[0]
        height = width_and_height[1]
        margin = file_grid["margin"]
        cell_size = file_grid["cell_size"]
        cell_amount = file_grid["cell_amount"]
        covered_cells = set(file_dict["covered_cells"])

        # create grid
        self.grid = Grid(cell_size, cell_amount, margin)

        # draw grid
        self.grid.draw_grid(screen)

        # make timer
        font = pygame.font.Font(None, 36)
        timer = Timer(font, int(width / 2), 36 / 2, 15)
        self.timer = timer

        # points
        points_p1 = Points(font, file_points["red"], 0.5 * margin, 50)
        points_p2 = Points(font, file_points["green"], width - 0.5 * margin, 50)
        self.points = {"red": points_p1, "green": points_p2}

        # player names
        self.name_player1 = file_dict["players"]["red"]
        self.name_player2 = file_dict["players"]["green"]

        # MAKE PLAYER BOARDs
        board_col = pygame.Color(10, 10, 10)
        p1_board = Board(board_col, 0, 0, margin, height)
        p2_board = Board(board_col, width - margin, 0, margin, height)
        self.boards = (p1_board, p2_board)

        # load images
        r_block_img = pygame.image.load(
            os.path.join(os.getcwd(), "images\\block_red.png")
        )
        g_block_img = pygame.image.load(
            os.path.join(os.getcwd(), "images\\block_green.png")
        )
        rotate_image = pygame.image.load(
            os.path.join(os.getcwd(), "images\\rotate.png")
        )
        rotate_img_model = Image(rotate_image, width / 2, 100, 80)
        self.rotate_img = rotate_img_model

        # make block + shape handler
        red_block = Block(
            self.grid.cell_size + 10,
            height - margin + self.grid.cell_size + 10,
            cell_size,
            r_block_img,
        )
        green_block = Block(
            width - margin + self.grid.cell_size + 10,
            height - margin + self.grid.cell_size + 10,
            cell_size,
            g_block_img,
        )
        self.shape_handler = ShapeHandler(
            {"red": red_block, "green": green_block}, int(margin - cell_size / 2)
        )

        # generate shapes
        self.next_shapes = {}
        for shape in file_shapes:
            shape_type = Shapes[shape["shape_type"]]
            game_shape = self.shape_handler.generate_shape(shape["col"], shape_type)
            game_shape.move(shape["pos"][0], shape["pos"][1])
            if shape == file_current_shape:
                self.current_shape = game_shape
                self.is_player_1 = self.current_shape.col == "red"
            elif shape["is_placed"]:
                game_shape.is_placed = True
            else:
                self.next_shapes[shape["col"]] = game_shape

        self.shape_handler.covered_cells = covered_cells

    def save_game(self) -> bool:
        def serialize(obj):
            if type(obj) == Block:
                return (obj.rect.centerx, obj.rect.centery)
            elif type(obj) == Points:
                return obj.points
            elif type(obj) == Shape:
                return {
                    "pos": (obj.x, obj.y),
                    "is_placed": obj.is_placed,
                    "col": obj.col,
                    "shape_type": obj.shape.name,
                }
            elif type(obj) == set:
                return list(obj)
            try:
                return obj.__dict__
            except:
                return None

        # dump shapes
        with open(self.save_path, "w") as file:
            json.dump(
                {
                    "current_shape": self.current_shape,
                    "shapes": self.shape_handler.all_shapes,
                    "covered_cells": self.shape_handler.covered_cells,
                    "grid": self.grid,
                    "points": self.points,
                    "players": {"red": self.name_player1, "green": self.name_player2},
                    "width_and_height": self.width_and_height,
                },
                file,
                default=serialize,
                indent=4,
            )

    def play_game(self, screen: pygame.surface) -> tuple:
        # music
        pygame.mixer.music.load(os.path.join(os.getcwd(), "sounds\\Tetris.mp3"))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)

        # main game loop
        game_over = False
        is_dragging_shape = False

        density = 0
        total_cells = self.grid.cell_amount**2

        while True:
            texts = pygame.sprite.Group(
                self.rotate_img,
                self.timer,
                self.points["red"],
                self.points["green"],
                self.boards[0].text,
                self.boards[1].text,
            )
            try:
                if game_over:
                    while True:
                        if self.points["red"].points > self.points["green"].points:
                            win_screen(
                                self.clock,
                                screen,
                                self.grid.cell_amount,
                                self.points["red"].points,
                                self.name_player1,
                            )
                        elif self.points["red"].points < self.points["green"].points:
                            win_screen(
                                self.clock,
                                screen,
                                self.grid.cell_amount,
                                self.points["green"].points,
                                self.name_player2,
                            )
                        else:
                            win_screen(self.clock, screen, self.grid.cell_amount)

                # if shape is placed generate new shape
                if self.current_shape.is_placed:
                    density = len(self.shape_handler.covered_cells) / total_cells * 100
                    self.timer.reset()
                    if self.is_player_1:
                        self.points["red"].add_points(self.current_shape.shape, density)
                        self.current_shape = self.next_shapes["green"]
                        self.current_shape.move(
                            self.width_and_height[0]
                            - self.grid.margin
                            + self.grid.cell_size,
                            int(self.width_and_height[1] / 2),
                        )
                        self.next_shapes["green"] = self.shape_handler.generate_shape(
                            "green"
                        )
                        self.is_player_1 = False
                    else:
                        self.points["green"].add_points(
                            self.current_shape.shape, density
                        )
                        self.current_shape = self.next_shapes["red"]
                        self.current_shape.move(
                            self.grid.cell_size, int(self.width_and_height[1] / 2)
                        )
                        self.next_shapes["red"] = self.shape_handler.generate_shape(
                            "red"
                        )
                        self.is_player_1 = True

                # player input
                if is_dragging_shape:
                    x, y = pygame.mouse.get_pos()
                    self.current_shape.move(x, y)
                for event in pygame.event.get():
                    match event.type:
                        case pygame.QUIT:
                            raise SystemExit
                        case pygame.MOUSEBUTTONUP:
                            is_dragging_shape = False
                            is_valid = True
                            item = self.current_shape.sprites()[0]
                            # if inside of a board it has no valid pos
                            for board in self.boards:
                                if board.is_xpos_in_board(x):
                                    is_valid = False
                                    break

                            # get closest grid and check if shape has valid pos
                            if (
                                item.rect.collidepoint(x, y)
                                or self.current_shape.shape == Shapes.S_BLOCK
                                or self.current_shape.shape == Shapes.Z_BLOCK_R
                                or self.current_shape.shape == Shapes.T_BLOCK
                                or self.current_shape.shape == Shapes.T_BLOCK_R
                                or self.current_shape.shape == Shapes.T_BLOCK_R2
                                or self.current_shape.shape == Shapes.L_BLOCK_R
                            ) and is_valid:
                                (
                                    closest_grid_x_and_y,
                                    closest_index,
                                ) = self.grid.closest_grid(x, y)
                                x, y = closest_grid_x_and_y
                                is_valid = self.shape_handler.check_is_valid_pos(
                                    x,
                                    y,
                                    self.current_shape.shape,
                                    self.grid.cell_amount,
                                    self.grid.cell_size,
                                    closest_index,
                                )
                                if is_valid:
                                    self.current_shape.move(x, y)
                                    self.current_shape.is_placed = True
                        case pygame.MOUSEBUTTONDOWN:
                            # what to do when mouse down
                            x, y = pygame.mouse.get_pos()
                            for item in self.current_shape.sprites():
                                if item.rect.collidepoint(x, y):
                                    is_dragging_shape = True
                                    break
                        case pygame.KEYDOWN:
                            match event.key:
                                case pygame.K_ESCAPE:
                                    resp = pause_screen(self.clock, screen)
                                    if resp != 1:
                                        if resp == 2:
                                            self.save_game()
                                        raise SystemExit
                                case pygame.K_r:
                                    if is_dragging_shape:
                                        rotate = True
                                        self.shape_handler.all_shapes.remove(
                                            self.current_shape
                                        )
                                        self.current_shape = (
                                            self.shape_handler.generate_shape(
                                                self.current_shape.col,
                                                self.current_shape.shape,
                                                rotate,
                                            )
                                        )

                # update screen
                self.grid.draw_grid(screen)
                for board in self.boards:
                    board.draw(screen)
                self.shape_handler.draw_shapes(screen)
                texts.draw(screen)

                pygame.display.flip()
                try:
                    self.timer.tick()
                except:
                    game_over = True
                self.clock.tick(60)
            finally:
                pass
