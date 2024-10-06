import random

class Civilization:
    def __init__(self, name, population, resources, technology):
        self.name = name
        self.population = population
        self.resources = resources
        self.technology = technology
        self.year = 0
        self.is_alive = True

    def progress(self):
        """Simulate one year of civilization progress."""
        if not self.is_alive:
            return
        
        self.year += 1
        print(f"Year {self.year}:")
        self.population_growth()
        self.resource_management()
        self.technological_advancement()
        self.random_events()
        self.check_collapse()
        self.status_report()

    def population_growth(self):
        """Simulate population growth."""
        growth_rate = random.uniform(0.01, 0.05)  # Random growth rate between 1% and 5%
        self.population += int(self.population * growth_rate)
        print(f"  Population has grown to {self.population}.")

    def resource_management(self):
        """Simulate resource consumption and discovery."""
        resource_consumption = int(self.population * 0.05)  # 5% of population consumes resources
        self.resources -= resource_consumption
        resource_discovery = random.randint(0, 500)  # Random chance to discover new resources
        self.resources += resource_discovery
        print(f"  Resources: {self.resources} (consumed {resource_consumption}, discovered {resource_discovery}).")

    def technological_advancement(self):
        """Simulate technological progress."""
        tech_growth = random.uniform(0.01, 0.03)  # Random tech progress rate between 1% and 3%
        self.technology += tech_growth
        print(f"  Technology level increased to {self.technology:.2f}.")

    def random_events(self):
        """Simulate random events such as wars, plagues, or environmental disasters."""
        event_chance = random.randint(1, 100)
        if event_chance <= 10:
            disaster = random.choice(["war", "plague", "famine", "natural disaster"])
            loss_percentage = random.uniform(0.1, 0.3)  # 10% to 30% loss in population or resources
            if disaster in ["war", "plague"]:
                population_loss = int(self.population * loss_percentage)
                self.population -= population_loss
                print(f"  A {disaster} occurred! Population decreased by {population_loss}.")
            else:
                resource_loss = int(self.resources * loss_percentage)
                self.resources -= resource_loss
                print(f"  A {disaster} occurred! Resources decreased by {resource_loss}.")

    def check_collapse(self):
        """Check if the civilization has collapsed due to lack of resources or population decline."""
        if self.population <= 0 or self.resources <= 0:
            self.is_alive = False
            print(f"  The civilization {self.name} has collapsed.")

    def status_report(self):
        """Print current status of the civilization."""
        print(f"  Status of {self.name}: Population = {self.population}, Resources = {self.resources}, Technology = {self.technology:.2f}\n")

# Simulate a civilization
def simulate_civilization():
    civ_name = "Atlantis"
    civ = Civilization(name=civ_name, population=1000, resources=5000, technology=1.0)

    # Simulate 100 years of civilization progress
    while civ.is_alive and civ.year < 100:
        civ.progress()

if __name__ == "__main__":
    simulate_civilization()
