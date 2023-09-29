from typing import List

from sqlalchemy import ForeignKey, Integer, String, Table, Column
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database import Base
from base.models import Source, Class

spell_to_spell_subschool = Table(
    "spell_to_spell_subschools",
    Base.metadata,
    Column("spell_id", ForeignKey("spells.id"), primary_key=True),
    Column("spell_subschool_id", ForeignKey("spell_subschools.id"), primary_key=True),
)


spell_to_spell_attribute = Table(
    "spell_to_spell_attributes",
    Base.metadata,
    Column("spell_id", ForeignKey("spells.id"), primary_key=True),
    Column("spell_attribute_id", ForeignKey("spell_attributes.id"), primary_key=True),
)


spell_to_spell_component = Table(
    "spell_to_spell_components",
    Base.metadata,
    Column("spell_id", ForeignKey("spells.id"), primary_key=True),
    Column("spell_component_id", ForeignKey("spell_components.id"), primary_key=True),
)


spell_to_spell_class_level = Table(
    "spell_to_spell_class_levels",
    Base.metadata,
    Column("spell_id", ForeignKey("spells.id"), primary_key=True),
    Column("spell_class_level_id", ForeignKey("spell_class_levels.id"), primary_key=True),
)


class SpellSchool(Base):
    __tablename__ = "spell_schools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)


class SpellSubSchool(Base):
    __tablename__ = "spell_subschools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, unique=True)

    school_id: Mapped[int] = mapped_column(ForeignKey("spell_schools.id"))
    school: Mapped["SpellSchool"] = relationship("SpellSchool")

    spells: Mapped[List["Spell"]] = relationship(
        secondary=spell_to_spell_subschool, back_populates="subschools"
    )


class SpellAttribute(Base):
    __tablename__ = "spell_attributes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)

    spells: Mapped[List["Spell"]] = relationship(
        secondary=spell_to_spell_attribute, back_populates="attributes"
    )


class SpellComponent(Base):
    __tablename__ = "spell_components"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    abbr: Mapped[str] = mapped_column(String, index=True)

    spells: Mapped[List["Spell"]] = relationship(
        secondary=spell_to_spell_component, back_populates="components"
    )


class SpellClassLevel(Base):
    __tablename__ = "spell_class_levels"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    spell_class: Mapped[Class] = relationship("Class")
    level: Mapped[int] = mapped_column(Integer)


class SpellCastingTime(Base):
    __tablename__ = "spell_casting_times"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)

    spells: Mapped[List["Spell"]] = relationship("Spell", back_populates="casting_time")


class SpellDuration(Base):
    __tablename__ = "spell_durations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)

    spells: Mapped[List["Spell"]] = relationship("Spell", back_populates="duration")


class SpellResistance(Base):
    __tablename__ = "spell_resistances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)

    spells: Mapped[List["Spell"]] = relationship("Spell", back_populates="duration")


class Spell(Base):
    __tablename__ = "spells"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True)

    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))
    source: Mapped["Source"] = relationship("Source")

    school_id: Mapped[int] = mapped_column(ForeignKey("spell_schools.id"))
    school: Mapped[SpellSchool] = relationship("SpellSchool")

    casting_time_id: Mapped[int] = mapped_column(ForeignKey("spell_casting_times.id"))
    casting_time: Mapped[SpellCastingTime] = relationship("SpellCastingTime")

    spell_resistance_id: Mapped[int] = mapped_column(ForeignKey("spell_resistances.id"))
    spell_resistance: Mapped[SpellResistance] = relationship("SpellCastingTime")

    casting_range: Mapped[str] = mapped_column(String, index=True)

    target: Mapped[str] = mapped_column(String, index=True)

    saving_throw: Mapped[str] = mapped_column(String, index=True)

    description: Mapped[str] = mapped_column(String, index=True)

    duration_id: Mapped[int] = mapped_column(ForeignKey("spell_durations.id"))
    duration: Mapped[SpellDuration] = relationship("SpellDuration")



    subschools: Mapped[List[SpellSubSchool]] = relationship(
        secondary=spell_to_spell_subschool, back_populates="spells"
    )

    attributes: Mapped[List[SpellAttribute]] = relationship(
        secondary=spell_to_spell_attribute, back_populates="spells"
    )

    components: Mapped[List[SpellComponent]] = relationship(
        secondary=spell_to_spell_component, back_populates="spells"
    )

    class_levels: Mapped[List[SpellClassLevel]] = relationship(
        secondary=spell_to_spell_component, back_populates="spells"
    )




