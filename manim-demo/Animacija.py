from manim import *


FONT = "Cambria"
DARK = "#202B3C"
BLUE = "#1769AA"
GREEN = "#16804A"
ORANGE = "#C65D0E"
GRAPH_BLUE = "#1769AA"


def make_car():
    body = RoundedRectangle(width=1.4, height=0.5, corner_radius=0.15,
                            fill_color=BLUE, fill_opacity=1, stroke_color=BLUE)
    top = RoundedRectangle(width=0.8, height=0.4, corner_radius=0.15,
                           fill_color="#58A6D8", fill_opacity=1, stroke_color="#58A6D8")
    top.next_to(body, UP, buff=-0.05)
    w1 = Circle(radius=0.17, fill_color=DARK, fill_opacity=1,
                stroke_color=WHITE, stroke_width=2)
    w2 = w1.copy()
    w1.move_to(body.get_bottom() + LEFT * 0.4)
    w2.move_to(body.get_bottom() + RIGHT * 0.4)
    return VGroup(body, top, w1, w2)


class Odvod(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ---------- 1. AVTO POSPEŠUJE ----------
        naslov = Text("Odvod: kako hitro se nekaj spreminja", font=FONT,
                      weight=SEMIBOLD, font_size=36, color=DARK).to_edge(UP, buff=0.35)
        self.play(Write(naslov), run_time=1.5)

        road = Line(LEFT * 6.5, RIGHT * 6.5, color="#64748B", stroke_width=8)
        road.shift(DOWN * 1.1)
        sredinska_crta = DashedLine(LEFT * 6.3, RIGHT * 6.3, color=WHITE,
                                    stroke_width=2, dash_length=0.25).shift(DOWN * 1.1)
        car_start = LEFT * 5.5 + DOWN * 0.65
        car = make_car().move_to(car_start)
        self.play(Create(road), Create(sredinska_crta), FadeIn(car))

        opis = Text("Model gibanja: s(t) = t²  |  t v sekundah, s v metrih",
                    font=FONT, font_size=25, color=DARK).move_to(DOWN * 2.15)
        self.play(FadeIn(opis))

        cas = ValueTracker(0)
        cas_label = Text("čas t =", font=FONT, font_size=24, color=DARK)
        cas_stevilo = DecimalNumber(0, num_decimal_places=1, font_size=28,
                                    color=DARK, unit=" s")
        cas_stevilo.add_updater(lambda m: m.set_value(cas.get_value()))
        hitrost_label = Text("hitrost v =", font=FONT, font_size=24, color=DARK)
        hitrost_stevilo = DecimalNumber(0, num_decimal_places=1, font_size=28,
                                        color=GREEN, unit=" m/s")
        hitrost_stevilo.add_updater(lambda m: m.set_value(2 * cas.get_value()))
        prikaz = VGroup(
            VGroup(cas_label, cas_stevilo).arrange(RIGHT, buff=0.12),
            VGroup(hitrost_label, hitrost_stevilo).arrange(RIGHT, buff=0.12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        prikaz.to_corner(UR, buff=0.55).shift(DOWN * 0.65)
        self.play(FadeIn(prikaz))

        self.play(
            cas.animate.set_value(5),
            UpdateFromAlphaFunc(
                car,
                lambda m, alpha: m.move_to(car_start + RIGHT * 10.5 * alpha ** 2),
                rate_func=linear,
            ),
            run_time=6,
            rate_func=linear,
        )
        self.wait(0.7)

        # ---------- 2. POT -> GRAF ----------
        self.play(FadeOut(car), FadeOut(road), FadeOut(sredinska_crta),
                  FadeOut(opis), FadeOut(prikaz), FadeOut(naslov))

        naslov_grafa = Text("Pot in čas: naklon grafa pove hitrost", font=FONT,
                            weight=SEMIBOLD, font_size=32, color=DARK)
        naslov_grafa.to_edge(UP, buff=0.35)
        self.play(FadeIn(naslov_grafa))

        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 25, 5],
            x_length=6.0, y_length=4.3,
            axis_config={"include_tip": True, "stroke_color": DARK,
                         "color": DARK, "tip_length": 0.15},
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        ).shift(LEFT * 2.8 + DOWN * 0.25)
        x_stevilke = VGroup(*[
            MathTex(str(i), color=DARK, font_size=22).next_to(
                axes.c2p(i, 0), DOWN, buff=0.1,
            )
            for i in range(0, 6)
        ])
        y_stevilke = VGroup(*[
            MathTex(str(i), color=DARK, font_size=22).next_to(
                axes.c2p(0, i), LEFT, buff=0.12,
            )
            for i in range(5, 26, 5)
        ])
        stevilke_osi = VGroup(x_stevilke, y_stevilke)
        oznaka_t = MathTex(r"t\;[\mathrm{s}]", color=DARK, font_size=30)
        oznaka_t.next_to(axes.c2p(5, 0), DOWN, buff=0.28)
        oznaka_s = MathTex(r"s\;[\mathrm{m}]", color=DARK, font_size=30)
        oznaka_s.next_to(axes.c2p(0, 25), UP, buff=0.18)
        osi_oznake = VGroup(oznaka_t, oznaka_s)
        self.play(Create(axes), Write(stevilke_osi), Write(osi_oznake), run_time=2)

        graf = axes.plot(lambda x: x ** 2, x_range=[0, 5], color=GRAPH_BLUE,
                         stroke_width=5)
        graf_oznaka = MathTex(r"s(t)=t^2", color=GRAPH_BLUE, font_size=32)
        graf_oznaka.next_to(axes.c2p(3.55, 17), LEFT, buff=0.15)
        self.play(Create(graf), run_time=3)
        self.play(Write(graf_oznaka))

        # ---------- 3. SEKANTA: POVPREČNA HITROST ----------
        t = ValueTracker(1)
        h = ValueTracker(1.5)

        dot = always_redraw(lambda: Dot(
            axes.c2p(t.get_value(), t.get_value() ** 2), color=GREEN, radius=0.09))
        dot2 = always_redraw(lambda: Dot(
            axes.c2p(t.get_value() + h.get_value(),
                     (t.get_value() + h.get_value()) ** 2),
            color=ORANGE, radius=0.085))

        def narisi_premico():
            tv, hv = t.get_value(), h.get_value()
            k = 2 * tv + hv
            x0 = max(0, tv - 0.8)
            x1 = min(5, tv + hv + 0.8)
            return axes.plot(lambda x: tv ** 2 + k * (x - tv),
                             x_range=[x0, x1], color=ORANGE, stroke_width=4)

        premica = always_redraw(narisi_premico)
        self.play(FadeIn(dot))

        panel1 = Text("SEKANTA\nPovprečna hitrost = njen naklon",
                      font=FONT, weight=SEMIBOLD, font_size=24,
                      line_spacing=0.9, color=DARK)
        panel1.move_to(RIGHT * 3.55 + UP * 1.75)
        povp_formula = MathTex(
            r"v_{\mathrm{povp}}=\frac{\Delta s}{\Delta t}",
            color=ORANGE, font_size=34,
        ).move_to(RIGHT * 3.55 + UP * 0.85)
        self.play(FadeIn(dot2), Create(premica), FadeIn(panel1), Write(povp_formula))
        self.wait(1.5)

        panel2 = Text("h = časovni razmik med točkama",
                  font=FONT, font_size=21, color=DARK)
        panel2.move_to(RIGHT * 3.55 + DOWN * 0.45)
        h_label = MathTex(r"h=", color=DARK, font_size=30)
        h_value = DecimalNumber(1.5, num_decimal_places=2, font_size=30,
                                color=ORANGE, unit=" s")
        h_value.add_updater(lambda m: m.set_value(h.get_value()))
        h_display = VGroup(h_label, h_value).arrange(RIGHT, buff=0.1)
        h_display.move_to(RIGHT * 3.55 + DOWN * 1.65)
        self.play(FadeIn(panel2), FadeIn(h_display))
        self.play(h.animate.set_value(0), run_time=10, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(dot2), FadeOut(panel1), FadeOut(panel2),
                  FadeOut(povp_formula), FadeOut(h_display))

        # ---------- 4. TANGENTA: TRENUTNA HITROST ----------
        panel3 = Text("TANGENTA\nNjen naklon je trenutna hitrost",
                      font=FONT, weight=SEMIBOLD, font_size=24,
                      line_spacing=0.9, color=GREEN)
        panel3.move_to(RIGHT * 3.55 + UP * 1.55)

        v_besedilo = Text("v =", font=FONT, weight=SEMIBOLD,
                          font_size=30, color=DARK)
        v_stevilo = DecimalNumber(2, num_decimal_places=1, font_size=36,
                                  color=GREEN, unit=" m/s")
        v_stevilo.add_updater(lambda m: m.set_value(2 * t.get_value()))
        v_skupina = VGroup(v_besedilo, v_stevilo).arrange(RIGHT, buff=0.15)
        v_skupina.move_to(RIGHT * 3.55 + UP * 0.45)
        self.play(FadeIn(panel3), FadeIn(v_skupina))
        self.wait(1)

        poteza = Text("Večji naklon → večja hitrost\n(avto pospešuje)",
                      font=FONT, font_size=22, color=DARK, line_spacing=0.9)
        poteza.move_to(RIGHT * 3.55 + DOWN * 1.0)
        self.play(FadeIn(poteza))
        self.play(t.animate.set_value(2.6), run_time=7, rate_func=linear)
        self.play(t.animate.set_value(0.3), run_time=4, rate_func=smooth)
        self.wait(0.5)

        # ---------- 5. SKLEP ----------
        self.play(FadeOut(panel3), FadeOut(poteza), FadeOut(v_skupina))
        self.play(t.animate.set_value(1.5), run_time=1.5)

        formula = MathTex(
            r"s'(t)=\lim_{h\to 0}\frac{s(t+h)-s(t)}{h}",
            font_size=29, color=DARK,
        ).move_to(RIGHT * 3.55 + UP * 1.15)
        formula_frame = SurroundingRectangle(
            formula, color=GRAPH_BLUE, buff=0.18, stroke_width=2.5,
        )
        rezultat = MathTex(
            r"v(t)=s'(t)=2t\;\mathrm{m/s}",
            font_size=36, color=GREEN,
        ).move_to(RIGHT * 3.55 + DOWN * 0.05)
        sklep = Text("Odvod je naklon tangente. Pove,\n"
                     "kako hitro se pot spreminja.",
                     font=FONT, font_size=22, line_spacing=0.9, color=DARK)
        sklep.move_to(RIGHT * 3.55 + DOWN * 1.35)
        self.play(Write(formula), Create(formula_frame), run_time=2.5)
        self.play(Write(rezultat), run_time=1.5)
        self.play(FadeIn(sklep))
        self.wait(3)