from engine.battle.move import LimitBreak, Move

# White Mage / Dog
revive = Move(name="Revive", description="Woof! {CASTER} revives {TARGET}!")
curaga = Move(
    name="Curaga",
    base_heal=99,
    default_to_target_self=True,
    description="Arf! {CASTER} tops off {TARGET}'s HP!",
)

# Astrologian
tunguska_impact = Move(
    name="Tunguska Impact",
    base_dmg=7,
    description="{CASTER} summons a 11,000 ton asteroid to explode over {TARGET}",
)
van_allen_radiation = Move(
    name="Van Allen Radiation",
    base_dmg=2,
    description="{CASTER} irradiates {TARGET} with cosmic rays",
)
space_junk = Move(
    name="Space Junk",
    base_dmg=3,
    description="{CASTER} drops a satelite on {TARGET}'s head",
)
tiny_commits = Move(
    name="Tiny Commits",
    base_heal=2,
    default_to_target_self=True,
    description="A flurry of tiny commits pads {TARGET}'s stats",
)

# Engineer
n_plus_one = Move(
    name="N+1",
    base_dmg=4,
    description="{TARGET} is overwhelmed by inefficent database queries",
)
clean_code = Move(
    name="Clean code",
    base_dmg=3,
    description="{TARGET} is blown away by the elegance of {CASTER}'s code",
)
changes_requested = Move(
    name="Changes Requested",
    base_dmg=6,
    description="{CASTER} requests a change to {TARGET}'s pull request",
)
refactoring = Move(
    name="Refactoring",
    base_heal=5,
    default_to_target_self=True,
    description="{CASTER} refactors {TARGET}'s code.  What relief!",
)

# Product Manager
changed_requirements = Move(
    name="Changed Requirements",
    base_dmg=2,
    description="{CASTER} updates the acceptance criteria for {TARGET}'s tickets",
)
product_launch = Move(
    name="Product Launch",
    base_dmg=7,
    description="{CASTER} launches the product at {TARGET}'s noggin",
)
figma_fury = Move(
    name="Figma Fury",
    base_dmg=4,
    description="{CASTER}'s buries {TARGET} in wireframes",
)
hard_deadline = Move(
    name="Hard Deadline",
    base_dmg=5,
    description="{CASTER}'s advances {TARGET}'s deadline",
)


# Salesperson
sqo_points = Move(
    name="SQO Points",
    base_dmg=5,
    description="{CASTER} barrages {TARGET} with a flurry of SQO points",
)
art_of_the_deal = Move(
    name="Art of the Deal",
    base_dmg=3,
    description="{CASTER} makes {TARGET} an offer they can't refuse",
)
coffee_is_for_closers = Move(
    name="Coffee is for closers",
    base_dmg=7,
    description="{CASTER} throws a macchiato at {TARGET}",
)
fat_commission = Move(
    name="Fat Commission",
    base_heal=3,
    default_to_target_self=True,
    description=(
        "{CASTER} earns a hefty commission, and treats themselves "
        "to some well-deserved self-care"
    ),
)


# New Hire
technical_interview_excellence = Move(
    name="Technical Interview Excellence",
    base_dmg=1,
    description="{CASTER} knows how to invert a binary tree",
)
willingness_to_learn = Move(
    name="Willingness to Learn",
    base_dmg=1,
    description="{CASTER} demonstrates their aptitude for learning",
)
doe_eyed_naivete = Move(
    name="Doe-Eyed Naivete",
    description="{CASTER} stares expectantly at {TARGET}, but nothing happens",
)
on_site_onboarding_per_diem = Move(
    name="On-Site Onboarding Per Diem",
    base_heal=1,
    default_to_target_self=True,
    description="{CASTER} eats a nutritious breakfast purchased with their per-diem.",
)


# Limit Breaks
supernova = LimitBreak(
    name="Supernova",
    base_dmg=99,
    description=(
        "{CASTER} channels his knowledge of arcane geometry to draw "
        "Alpha Centauri into our sun.  A blinding stellar explosion "
        "envelops Mercury and Venus.  The stratosphere ignites into an "
        "inferno of red-hot plasma."
    ),
)
crippling_anxiety = LimitBreak(
    name="Crippling Anxiety",
    base_dmg=99,
    description=(
        "{CASTER} curls up in the fetal position and begins hyperventilating. "
        "{CASTER} begins rolling around the room at ever greater speeds. With "
        "a sharp CRACK {CASTER} breaks the sound barrier and collides with {TARGET}"
    ),
)
jira_mastery = LimitBreak(
    name="Jira Mastery",
    base_dmg=99,
    description=(
        "The sky darkens.  A cloud of Jira tickets blots out "
        "the sun. {TARGET} is overwhelmed by 9999 story points."
    ),
)
smooth_talkin = LimitBreak(
    name="Smooth Talkin'",
    base_dmg=99,
    description=(
        "What a voice! What charisma! You can't say 'no' to "
        "that! {CASTER} bankrupts {TARGET} with a 170k USD upsell."
    ),
)
core_values_alignment = LimitBreak(
    name="Core Value Alignment",
    base_dmg=99,
    description=(
        "{CASTER}'s soul shines brightly. Five stars of pure virtue align. {CASTER} "
        "anihilates {TARGET} with twin beams of Kindness and Authenticity."
    ),
)
woof = LimitBreak(name="Woof")
