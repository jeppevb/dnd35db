import logging
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import Spell as DtoSpell
from ..database import SessionLocal

log = logging.getLogger(__name__)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/spell",
    response_model=List[DtoSpell],
    summary="Retrieves a list of spells.",
)
def get_query_spell(name_filter: Optional[str] = None,
                    sources: Optional[list[str]] = None,
                    description_filter: Optional[str] = None,
                    casting_time_filter: Optional[str] = None,
                    spell_resistance_filter: Optional[str] = None,
                    casting_range_filter: Optional[str] = None,
                    target_filter: Optional[str] = None,
                    saving_throw_filter: Optional[str] = None,
                    material_components: Optional[list[str]] = None,
                    duration_filter: Optional[str] = None,
                    class_levels: Optional[list[str]] = None,
                    db_session: Session = Depends(get_db)) -> List[DtoSpell]:
    """Retrieves a list of subjects."""
    return [DtoSpell(name=s.name, smersh=smersh, rating=s.rating) for s in get_spells(name_filter, sources,
                    description_filter, casting_time_filter, spell_resistance_filter,
                    casting_range_filter,
                    target_filter,
                    saving_throw_filter,
                    material_components,
                    duration_filter,
                    class_levels, db_session)]


@router.post(
    "/",
    response_model=str,
    summary="Creates a smersh with a list of subjects.",
)
def post_root(smersh: CreateSmersh, db_session: Session = Depends(get_db)) -> str:
    """Retrieves a list of subjects."""
    create_smersh(smersh, db_session)
    return "OK"


@router.post(
    "/{smersh}/vote",
    response_model=str,
    summary="Votes"
)
def post_vote(smersh: str, vote: DtoVoteInput, db_session: Session = Depends(get_db)):
    assert check_user_exists(vote.voter, db_session), "User not found"
    register_vote(smersh, vote, db_session)
    return "OK"


@router.post(
    "/{smersh}",
    response_model=str,
    summary="Create subject"
)
def post_subject(smersh: str, subject: DtoSubjectInput, db_session: Session = Depends(get_db)):
    create_subject(subject, smersh, db_session)
    return "OK"


@router.post(
    "/user",
    response_model=str,
    summary="Creates a user"
)
def post_user(user_name: str, db_session: Session = Depends(get_db)):
    return "OK"

@router.get(
    "/{smersh}/vote",
    response_model=DtoMatchup,
    summary="Retrieves a matchup",
)
def get_subjects(smersh, db_session: Session = Depends(get_db)) -> DtoMatchup:
    """Retrieves a list of subjects."""
    var = get_matchup(smersh, db_session)
    return DtoMatchup(subject_a=var[0], subject_b=var[1])


