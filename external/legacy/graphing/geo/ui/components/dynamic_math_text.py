"""
self.equation = MathTex(r"A = \text{const}").move_to(self.equation_position)
        
        self.equation_numbers = MathTex("A").move_to(self.equation_numbers_position)
        self.equation_numbers.add_updater(lambda obj: obj.become(
            MathTex(f"{np.round(self.a_length.get_value(), 2)} : {np.round(self.b_length.get_value(), 2)} = 0.77").move_to(self.equation_numbers_position)
        ))

"""