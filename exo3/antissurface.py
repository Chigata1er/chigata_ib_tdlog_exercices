from classe_mère import weapon

class Lance_missiles_antisurface(weapon):
    def method_abstraite(self,type: int,rayon: int,munition: int):
        type = super.fire_at()

a = Lance_missiles_antisurface()
print(a.type)
        