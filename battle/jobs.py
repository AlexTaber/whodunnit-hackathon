import battle.moves as moves
from engine.battle.job import Job

white_mage_dog = Job(
    name="White Mage / Dog",
    motto="a very good boy",
    moves=[
        moves.revive,
        moves.curaga,
    ],
    limit_break=moves.woof,
    base_intelligence=5,
    base_charisma=5,
    base_stamina=5,
    base_people_skills=5,
)

astrologian = Job(
    name="Astrologian",
    motto="master of the universe",
    moves=[
        moves.tunguska_impact,
        moves.van_allen_radiation,
        moves.space_junk,
        moves.tiny_commits,
    ],
    limit_break=moves.supernova,
    base_intelligence=5,
    base_charisma=1,
    base_stamina=5,
    base_people_skills=2,
)

engineer = Job(
    name="Engineer",
    motto="master of code",
    moves=[
        moves.n_plus_one,
        moves.clean_code,
        moves.changes_requested,
        moves.refactoring,
    ],
    limit_break=moves.crippling_anxiety,
    base_intelligence=5,
    base_charisma=0,
    base_stamina=4,
    base_people_skills=1,
)

product_manager = Job(
    name="Product Manager",
    motto="master of product",
    moves=[
        moves.changed_requirements,
        moves.product_launch,
        moves.figma_fury,
        moves.hard_deadline,
    ],
    limit_break=moves.jira_mastery,
    base_intelligence=3,
    base_charisma=1,
    base_stamina=5,
    base_people_skills=3,
)

salesperson = Job(
    name="Salesperson",
    motto="master of sales",
    moves=[
        moves.sqo_points,
        moves.art_of_the_deal,
        moves.coffee_is_for_closers,
        moves.fat_commission,
    ],
    limit_break=moves.smooth_talkin,
    base_intelligence=2,
    base_charisma=5,
    base_stamina=3,
    base_people_skills=4,
)

new_hire = Job(
    name="New Hire",
    motto="master of none",
    moves=[
        moves.technical_interview_excellence,
        moves.willingness_to_learn,
        moves.doe_eyed_naivete,
        moves.on_site_onboarding_per_diem,
    ],
    limit_break=moves.core_values_alignment,
    base_intelligence=0,
    base_charisma=0,
    base_stamina=0,
    base_people_skills=0,
)
