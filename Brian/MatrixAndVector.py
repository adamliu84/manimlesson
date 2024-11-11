from manim import *

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True,
        )

    def construct(self):

        # matrix = [[1, 2], [2, 1]]
        rotation_matrix = [[0,1],[-1,0]]

        matrix_tex = (
            MathTex("A = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        unit_square = self.get_unit_square()
        text = always_redraw(
            lambda: Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center())
        )

        vect = self.get_vector([1, -2], color=PURPLE_B)

        rect1 = Rectangle(
            height=2, width=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6
        ).shift(UP * 2 + LEFT * 2)

        circ1 = Circle(
            radius=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6
        ).shift(DOWN * 2 + RIGHT * 1)

        self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(rotation_matrix)
        # https://stackoverflow.com/questions/71587568/how-do-i-apply-multiple-linear-transformations
        self.moving_mobjects = []

        reflection_matrix = [[1, 0], [0, -1]]
        self.apply_matrix(reflection_matrix)
        self.moving_mobjects = []

        stretching_matrix = [[0.5,0],[0,0.5]]
        self.apply_matrix(stretching_matrix)
        self.moving_mobjects = []

        self.apply_inverse(stretching_matrix)
        self.moving_mobjects = []

        self.wait()