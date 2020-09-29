from manimlib.imports import *

class DogObject():
    def __init__(self,var_name,address):
        self.var_name = var_name
        self.address = address

class RectangleExhibit(Scene):
    def construct(self):
        adog = DogObject('adog','1234')
        olddog = DogObject('olddog','9879')
        self.dogs = [adog,olddog]

        self.first_obj = TextMobject('"Max"')
        self.first_obj.add_background_rectangle()
        self.rect = SurroundingRectangle(self.first_obj)
        self.rect.set_color(BLUE)

        label = TextMobject('dog object')
        label.next_to(self.first_obj,DOWN)

        self.second_obj = TextMobject('"Fifi"')
        self.second_obj.next_to(label,DOWN)
        self.second_obj.add_background_rectangle()
        self.rect_two = SurroundingRectangle(self.second_obj)
        self.rect_two.set_color(YELLOW)

        self.label_two = TextMobject('dog object')
        self.label_two.next_to(self.second_obj,DOWN)


        self.play(
            ShowCreation(self.rect),
            # ShowCreation(label_dog_address),
            ShowCreation(self.first_obj),
            ShowCreation(label),
        )
        self.create_first_obj()
        # self.add_block_creators()
        self.create_arrows()
        self.update_arrow()
        self.wait()


    def get_block(self,dog):
        # block = Rectangle(
        #     color = WHITE,
        #     height = 1,
        #     width = 2,
        # )


        address = TextMobject(dog.address)
        address.add_background_rectangle()

        # for vect in UP, DOWN:
        #     line = Line(block.get_left(), block.get_right())
        #     line.shift(0.3*block.get_height()*vect)
        #     block.add(line)
        return address

    def create_first_obj(self):
        
        blocks = VGroup(*[
            self.get_block(dog) for dog in self.dogs
        ])
        blocks.arrange(DOWN, buff = 1.5)
        blocks.to_edge(LEFT)

        rects = VGroup()
        for block in blocks:
            block.add_background_rectangle()
            rect = SurroundingRectangle(block)
            rect.set_color(RED)
            rects.add(rect)

        var_names = VGroup()
        for dog,block in zip(self.dogs,blocks):
            var_name = TextMobject(dog.var_name)
            var_name.next_to(block,DOWN)
            var_names.add(var_name)
            
        self.rects = rects
        self.blocks = blocks
    
        self.play(
                FadeIn(blocks[0]),
                ShowCreation(rects[0]),
                FadeIn(var_names[0])
                )
        # self.play(
        #         LaggedStartMap(FadeIn, blocks),
        #         ShowCreation(rects),
        #         LaggedStartMap(FadeIn, var_names)
        #         )


    def create_arrows(self):
        arrows = VGroup()
        for block in self.blocks:
            arrow = Arrow(block.get_right(),self.first_obj.get_left())
            arrows.add(arrow)
            self.last_arrow = arrow

        self.play(GrowArrow(arrows[0]))

    def update_arrow(self):
        self.remove(self.last_arrow)
        last_block = self.blocks[-1]
        arrow = Arrow(last_block.get_right(),self.second_obj.get_left())

        # self.play(
        #         GrowArrow(arrow)
        #         )
