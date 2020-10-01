from manimlib.imports import *

class DogObject():
    def __init__(self,var_name,address):
        self.var_name = var_name
        self.address = address

class RectangleExhibit(Scene):

    def construct(self):
        adog = DogObject('adog','7889')
        olddog = DogObject('olddog','7889')
        d = DogObject('d','7889') 
        self.dogs = [adog,olddog,d]

        self.create_dog_objects()
        self.create_instances()
        self.create_arrows()

        self.show_first_assignment()
        self.show_second_assignment()

        self.show_function_call()
        self.update_arrow()
        self.wait(3)

    def get_block(self,dog):
        address = TextMobject(dog.address)
        address.add_background_rectangle()
        return address

    def create_dog_objects(self):
        self.first_obj = TextMobject('"Max"')
        self.first_obj.add_background_rectangle()
        self.rect = SurroundingRectangle(self.first_obj)
        self.rect.set_color(BLUE)

        self.label_one = TextMobject('dog object')
        self.label_one.next_to(self.first_obj,UP)

        self.address_label_one = TextMobject('7889')
        self.address_label_one.next_to(self.first_obj,DOWN)


        self.label_two = TextMobject('dog object')
        self.label_two.next_to(self.address_label_one,DOWN)

        self.second_obj = TextMobject('"Fifi"')
        self.second_obj.next_to(self.label_two,DOWN)
        self.second_obj.add_background_rectangle()
        self.rect_two = SurroundingRectangle(self.second_obj)
        self.rect_two.set_color(YELLOW)

        self.address_label_two = TextMobject('6477')
        self.address_label_two.next_to(self.second_obj,DOWN)

        self.wait(1)

    def create_instances(self):
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
        self.var_names = var_names
    

    def create_arrows(self):
        arrows = VGroup()
        for block in self.blocks:
            arrow = Arrow(block.get_right(),self.first_obj.get_left())
            arrows.add(arrow)

        self.arrows = arrows

    def show_first_assignment(self):
        self.play(
                FadeIn(self.blocks[0]),
                ShowCreation(self.rects[0]),
                FadeIn(self.var_names[0])
                )

        self.wait(1)
        self.play(
            ShowCreation(self.rect),
            ShowCreation(self.first_obj),
            ShowCreation(self.label_one),
            ShowCreation(self.address_label_one),
            
        )
        self.wait(1)
        self.play(GrowArrow(self.arrows[0]))
        self.wait(1)

    def show_second_assignment(self):
        self.play(
                FadeIn(self.blocks[1]),
                ShowCreation(self.rects[1]),
                FadeIn(self.var_names[1])
                )
        self.wait(1)
        self.play(
                GrowArrow(self.arrows[1])
                )
        self.wait(1)


    def show_second_instance(self):
        self.play(
                FadeIn(self.blocks[-1]),
                ShowCreation(self.rects[-1]),
                FadeIn(self.var_names[-1]),
                )
        self.wait(1)
        self.play(GrowArrow(self.arrows[1]))
        self.wait(1)


    def show_function_call(self):
        self.play(
                FadeIn(self.blocks[-1]),
                ShowCreation(self.rects[-1]),
                FadeIn(self.var_names[-1])
                )
        self.wait(1)
        self.play(GrowArrow(self.arrows[-1]))
        self.wait(1)

    def update_arrow(self):
        self.play(
                FadeIn(self.label_two),
                FadeIn(self.second_obj),
                FadeIn(self.rect_two),
                FadeIn(self.address_label_two)
                )
        self.wait(1)
        updated_pointer_address = TextMobject('6477')
        updated_pointer_address.add_background_rectangle()
        updated_pointer_address.move_to(self.blocks[-1])
        self.play(
                Transform(self.blocks[-1],updated_pointer_address),
                )
        self.wait(1)
        self.play(
                FadeOut(self.arrows[-1])
                )
        self.wait(1)

        self.remove(self.arrows[-1])
        last_block = self.blocks[-1]
        arrow = Arrow(last_block.get_right(),self.second_obj.get_left())

        self.play(
                GrowArrow(arrow)
                )
