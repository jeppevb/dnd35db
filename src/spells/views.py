import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import Subject as DtoSubject, BaseSubject as DtoSubjectInput, VoteInput as DtoVoteInput, Matchup as DtoMatchup, Smersh as CreateSmersh
from .service import get, check_user_exists, vote as register_vote, get_matchup, create_smersh, create_subject

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
    "/{smersh}",
    response_model=List[DtoSubject],
    summary="Retrieves a list of subjects.",
)
def get_root(smersh: str, db_session: Session = Depends(get_db)) -> List[DtoSubject]:
    """Retrieves a list of subjects."""
    return [DtoSubject(name=s.name, smersh=smersh, rating=s.rating) for s in get(smersh, db_session)]


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


