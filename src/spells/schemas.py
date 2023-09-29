from pydantic import BaseModel


class Spell(BaseModel):
    name: str
    source: str
    school: str
    subschools: list[str]
    attributes: list[str]
    casting_time: str
    spell_resistance: str
    casting_range: str
    target: str
    saving_throw: str
    description: str
    material_components: list[str]
    duration: str
    class_levels: list[str]
