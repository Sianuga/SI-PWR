from experta import *

class DishwasherComponent(Fact):
    """Represents physical components of the dishwasher"""
    name = Field(str, mandatory=True)

class RequiredItem(Fact):
    """Items necessary for operating the dishwasher"""
    type = Field(str, mandatory=True)
    status = Field(str, default="available")  # Possible statuses: available, unavailable

class DishSetting(Fact):
    """Settings that can be adjusted on the dishwasher"""
    name = Field(str, mandatory=True)
    status = Field(str, default="proper")  # Possible statuses: proper, improper

class Problem(Fact):
    """Problems that might occur"""
    description = Field(str, mandatory=True)

class Solution(Fact):
    """Solutions to the problems identified"""
    description = Field(str, mandatory=True)

class Dishes(Fact):
    """Dishes to be washed"""
    state = Field(str, mandatory=True)  # Possible states: clean, unclean

class DishwasherExpert(KnowledgeEngine):
    @DefFacts()
    def essential_components(self):
        """Initial facts about required components and items"""
        yield DishwasherComponent(name="water inlet valve")
        yield DishwasherComponent(name="heating element")
        yield DishwasherComponent(name="spray arms")
        yield DishwasherComponent(name="drain pump")
        yield DishwasherComponent(name="detergent dispenser")
        yield DishwasherComponent(name="control panel")
        yield DishwasherComponent(name="door latch")
        yield DishSetting(name="wash cycle", status="proper")

    @Rule(AND(Dishes(state="unclean"),
              RequiredItem(type="detergent", status="available"),
              RequiredItem(type="rinse aid", status="available"),
              RequiredItem(type="salt", status="available"),
              DishSetting(name="wash cycle", status="proper")))
    def wash_dishes(self):
        print("Washing the dishes...")
        self.modify(self.facts[1], state="clean")
        print("Dishes are now clean.")

    @Rule(AND(Dishes(state="unclean"),
              OR(RequiredItem(type="detergent", status="unavailable"),
                 RequiredItem(type="rinse aid", status="unavailable"),
                 RequiredItem(type="salt", status="unavailable"))))
    def cannot_wash_dishes(self):
        print("Cannot wash dishes: Missing required items.")
        for fact in self.facts:
            if isinstance(fact, RequiredItem) and fact["status"] == "unavailable":
                print(f"{fact['type']} is unavailable.")

    @Rule(AND(RequiredItem(type="rinse aid", status="unavailable"),
              DishSetting(name="wash cycle", status="proper")))
    def check_rinse_aid(self):
        print("Rinse aid is required for optimal drying and shine. Please refill.")

    @Rule(AND(Problem(description="dishes not drying properly"),
              RequiredItem(type="rinse aid", status="unavailable")))
    def suggest_rinse_aid_solution(self):
        print("Ensure rinse aid is refilled to improve drying.")

    @Rule(AND(Problem(description="white residue on dishes"),
              RequiredItem(type="salt", status="unavailable")))
    def suggest_salt_solution(self):
        print("Refill salt to soften the water and prevent white residue.")

    @Rule(AND(Problem(description="dishwasher doesn’t start"),
              DishwasherComponent(name="control panel")))
    def check_control_panel(self):
        print("Check if the dishwasher is plugged in and the control panel is set correctly.")

    @Rule(AND(Problem(description="dishes remain dirty"),
              DishwasherComponent(name="spray arms")))
    def clean_spray_arms(self):
        print("Clean the spray arms to ensure they are not clogged with food particles.")

    @Rule(AND(Problem(description="water not draining"),
              DishwasherComponent(name="drain pump")))
    def check_drain_pump(self):
        print("Check the drain pump for blockages.")

    @Rule(AND(RequiredItem(type="rinse aid", status="unavailable"),
              RequiredItem(type="salt", status="unavailable"),
              DishSetting(name="wash cycle", status="proper")))
    def check_multiple_missing_items(self):
        print("Both rinse aid and salt are unavailable. Refill both to ensure proper washing and drying.")

  
    @Rule(AND(Problem(description="dishes remain dirty"),
              Problem(description="water not draining"),
              DishwasherComponent(name="spray arms"),
              DishwasherComponent(name="drain pump")))
    def handle_multiple_problems(self):
        print("Multiple issues detected: dishes remain dirty and water is not draining.")
        print("Clean the spray arms and check the drain pump for blockages.")


if __name__ == "__main__":
    engine = DishwasherExpert()
    engine.reset()

    print("Test case: Proper operation")
    engine.declare(RequiredItem(type="detergent", status="available"))
    engine.declare(RequiredItem(type="rinse aid", status="available"))
    engine.declare(RequiredItem(type="salt", status="available"))
    
    engine.declare(Dishes(state="unclean"))
    engine.run()

    print("\nTest case: Missing required items")
    engine.reset()
    engine.declare(RequiredItem(type="detergent", status="available"))
    engine.declare(RequiredItem(type="rinse aid", status="unavailable"))
    engine.declare(RequiredItem(type="salt", status="available"))
    engine.declare(Dishes(state="unclean"))
    engine.run()

    print("\nTest case: Rinse aid refill")
    engine.reset()
    engine.declare(Problem(description="dishes not drying properly"))
    engine.run()

    print("\nTest case: White residue on dishes")
    engine.reset()
    engine.declare(Problem(description="white residue on dishes"))
    engine.run()

    print("\nTest case: Dishwasher doesn’t start")
    engine.reset()
    engine.declare(Problem(description="dishwasher doesn’t start"))
    engine.run()

    print("\nTest case: Dishes remain dirty")
    engine.reset()
    engine.declare(Problem(description="dishes remain dirty"))
    engine.run()

    print("\nTest case: Water not draining")
    engine.reset()
    engine.declare(Problem(description="water not draining"))
    engine.run()

    engine.reset()


    print("\nTest case: Multiple missing items")
    engine.declare(RequiredItem(type="detergent", status="available"))
    engine.declare(RequiredItem(type="rinse aid", status="unavailable"))
    engine.declare(RequiredItem(type="salt", status="unavailable"))
    engine.declare(Dishes(state="unclean"))
    engine.run()

    engine.reset()

 
    print("\nTest case: Multiple problems")
    engine.declare(Problem(description="dishes remain dirty"))
    engine.declare(Problem(description="water not draining"))
    engine.run()
