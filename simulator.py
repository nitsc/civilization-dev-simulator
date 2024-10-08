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
        growth_rate = random.uniform(0.0001, 0.018)  # Random growth rate between 0.01% and 1.8%
        self.population += int(self.population * growth_rate)
        print(f"  Population has grown to {self.population}.")

    def resource_management(self):
        base_consumption_rate = 0.01  # 基本消耗率为1%
        consumption_rate = base_consumption_rate / (1 + self.technology)  # 随技术进步减少资源消耗
        resource_consumption = int(self.population * consumption_rate)
        self.resources -= resource_consumption
        resource_discovery = random.randint(0, 10**3*int(self.technology))  # 随技术进步增加资源发现量
        self.resources += resource_discovery
        print(f"  Resources: {self.resources} (consumed {resource_consumption}, discovered {resource_discovery}).")

    def technological_advancement(self):
        """Simulate technological progress."""
        tech_growth = random.uniform(0.01, 0.05)  # Random tech progress rate between 1% and 5%
        self.technology += tech_growth
        print(f"  Technology level increased to {self.technology:.2f}.")

    def random_events(self):
        """Simulate random events such as wars, plagues, or environmental disasters."""
        event_chance = random.randint(1, 100)
        if event_chance <= 10:
            disaster = random.choice(["war", "plague", "famine", "natural disaster"])
            loss_percentage = random.uniform(0.001, 0.2)  # 0.1% to 20% loss in population or resources
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

# Simulate a civilization with user-specified years
def simulate_civilization():
    civ_name = "Trisolaran"
    civ = Civilization(name=civ_name, population=100, resources=300, technology=0.1)

    # Ask the user for the number of years to simulate
    max_years = int(input("Enter the number of years you want to simulate: "))

    # Simulate civilization progress for the specified number of years
    while civ.is_alive and civ.year < max_years:
        civ.progress()

if __name__ == "__main__":
    simulate_civilization()
