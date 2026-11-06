from manim import *


class Demo(Scene):
    def construct(self):
        square = Square()
        formula = MathTex(r"e^{i\pi} + 1 = 0").next_to(square, DOWN)
        self.play(Create(square), run_time=2)
        self.play(Write(formula), run_time=2)
        self.wait()
        self.play(Transform(square, Circle(color=BLUE)), run_time=2)
        self.play(square.animate.set_fill(BLUE, opacity=0.5))
        self.play(formula.animate.scale(1.5).set_color(YELLOW))
        self.wait(2)
        self.play(FadeOut(square, formula))


# Ta del kode izdela animacijo, ko datoteko poženete z gumbom ▶ v
# urejevalniku VS Code.  Če animacijo izdelujete z ukazom `uv run manim`,
# ga lahko izbrišete.
if __name__ == "__main__":
    with tempconfig({"quality": "low_quality", "preview": True}):
        Demo().render()