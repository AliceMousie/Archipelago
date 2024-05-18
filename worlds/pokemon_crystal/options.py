from Options import Toggle, Choice, DefaultOnToggle, Range, PerGameCommonOptions
from dataclasses import dataclass


class Goal(Choice):
    """Elite Four: collect 8 badges and enter the Hall of Fame
        Red: collect 16 badges and defeat Red at Mt. Silver"""
    display_name = "Goal"
    default = 0
    option_elite_four = 0
    option_red = 1


class JohtoOnly(Toggle):
    """Excludes all of Kanto, disables early Kanto access
        Forces Goal to Elite Four and Badges to ≤8"""
    display_name = "Johto Only"
    default = 0


class EliteFourBadges(Range):
    """Number of badges required to enter Victory Road"""
    display_name = "Elite Four Badges"
    default = 8
    range_start = 1
    range_end = 16


class RedBadges(Range):
    """Number of badges required to open Silver Cave"""
    display_name = "Red Badges"
    default = 16
    range_start = 1
    range_end = 16


class RandomizeBadges(Choice):
    """Shuffles badges into the pool"""
    display_name = "Randomize Badges"
    default = 2
    option_vanilla = 0
    option_shuffle = 1
    option_completely_random = 2


class RandomizeHiddenItems(Toggle):
    """Shuffles hidden items into the pool"""
    display_name = "Randomize Hidden Items"
    default = 0


class RequireItemfinder(DefaultOnToggle):
    """Hidden items require Itemfinder in logic"""
    display_name = "Require Itemfinder"


class Trainersanity(Toggle):
    """Adds checks for defeating trainers"""
    display_name = "Trainersanity"
    default = 0


class RandomizePokegear(Toggle):
    """Shuffles the Pokegear and cards into the pool"""
    display_name = "Randomize Pokegear"
    default = 0


class RandomizeStarters(Choice):
    """Randomizes species of starter Pokemon"""
    display_name = "Randomize Starters"
    default = 0
    option_vanilla = 0
    option_unevolved_only = 1
    option_completely_random = 2


class RandomizeWilds(Toggle):
    """Randomizes species of wild Pokemon"""
    display_name = "Randomize Wilds"
    default = 0


class NormalizeEncounterRates(Toggle):
    """Normalizes chance of encountering each wild Pokemon slot"""
    display_name = "Normalize Encounter Rates"
    default = 0


class RandomizeStaticPokemon(Toggle):
    """Randomizes species of static Pokemon encounters"""
    display_name = "Randomize Static Pokemon"


class RandomizeTrainerParties(Choice):
    """Randomizes Pokemon in enemy trainer parties"""
    display_name = "Randomize Trainer Parties"
    default = 0
    option_vanilla = 0
    option_match_types = 1
    option_completely_random = 2


class RandomizeLearnsets(Choice):
    """vanilla: Vanilla movesets
    randomize: Random movesets
    start_with_four_moves: Random movesets with 4 starting moves"""
    display_name = "Randomize Learnsets"
    default = 0
    option_vanilla = 0
    option_randomize = 1
    option_start_with_four_moves = 2


class TMCompatibility(Range):
    """Percent chance for Pokemon to be compatible with a TM"""
    default = 0
    range_start = 0
    range_end = 100
    special_range_names = {
        "vanilla": 0,
        "fully_compatible": 100
    }


class HMCompatibility(Range):
    """Percent chance for Pokemon to be compatible with a HM"""
    default = 0
    range_start = 0
    range_end = 100
    special_range_names = {
        "vanilla": 0,
        "fully_compatible": 100
    }


class RandomizeBaseStats(Choice):
    """vanilla: Vanilla base stats
    keep_bst: Random base stats, but base stat total is preserved
    completely_random: Base stats and BST are completely random"""
    display_name = "Randomize Base Stats"
    default = 0
    option_vanilla = 0
    option_keep_bst = 1
    option_completely_random = 2


class RandomizeTypes(Choice):
    """vanilla: Vanilla Pokemon types
    follow_evolutions: Types are randomized but preserved when evolved
    completely_random: Types are completely random"""
    display_name = "Randomize Types"
    default = 0
    option_vanilla = 0
    option_follow_evolutions = 1
    option_completely_random = 2


class RandomizePalettes(Choice):
    """vanilla: Vanilla Pokemon color palettes
    match_types: Color palettes match Pokemon Type
    completely_random: Color palettes are completely random"""
    display_name = "Randomize Palettes"
    default = 0
    option_vanilla = 0
    option_match_types = 1
    option_completely_random = 2


class HMBadgeRequirements(Choice):
    """vanilla: HMs require their vanilla badges
    no_badges: HMs do not require a badge to use
    add_kanto: HMs can be used with the Johto or Kanto badge"""
    display_name = "HM Badge Requirements"
    default = 0
    option_vanilla = 0
    option_no_badges = 1
    option_add_kanto = 2


class ReusableTMs(Toggle):
    """TMs can be used an infinite number of times"""
    display_name = "Reusable TMs"
    default = 0


class GuaranteedCatch(Toggle):
    """Balls have a 100% success rate"""
    display_name = "Guaranteed Catch"
    default = 0


class MinimumCatchRate(Range):
    """Sets a minimum catch rate for wild Pokemon"""
    display_name = "Minimum Catch Rate"
    default = 0
    range_start = 0
    range_end = 255


class BlindTrainers(Toggle):
    """Trainers have no vision and will not start battles unless interacted with"""
    display_name = "Blind Trainers"
    default = 0


class BetterMarts(Toggle):
    """Improves the selection of items at Pokemarts"""
    display_name = "Better Marts"
    default = 0


class ExpModifier(Range):
    """Scale the amount of Experience Points given in battle.
    Default is 20, for double set to 40, for half set to 10, etc.
    Must be between 1 and 255"""
    display_name = "Experience Modifier"
    default = 20
    range_start = 1
    range_end = 255


class PhoneTrapWeight(Range):
    """Adds random Pokegear calls as traps"""
    display_name = "Phone Trap Weight"
    default = 0
    range_start = 0
    range_end = 8


class SleepTrapWeight(Range):
    """Trap that causes Sleep status on your party"""
    display_name = "Sleep Trap Weight"
    default = 0
    range_start = 0
    range_end = 8


class PoisonTrapWeight(Range):
    """Trap that causes Poison status on your party"""
    display_name = "Poison Trap Weight"
    default = 0
    range_start = 0
    range_end = 8


class BurnTrapWeight(Range):
    """Trap that causes Burn status on your party"""
    display_name = "Burn Trap Weight"
    default = 0
    range_start = 0
    range_end = 8


class FreezeTrapWeight(Range):
    """Trap that causes Freeze status on your party"""
    display_name = "Freeze Trap Weight"
    default = 0
    range_start = 0
    range_end = 8


class ParalysisTrapWeight(Range):
    """Trap that causes Paralysis status on your party"""
    display_name = "Paralysis Trap Weight"
    default = 0
    range_start = 0
    range_end = 8


class ItemReceiveSound(DefaultOnToggle):
    """Play item received sound on receiving a remote item"""
    display_name = "Item Receive Sound"


class EnableMischief(Toggle):
    """If I told you what this does, it would ruin the surprises :)"""
    display_name = "Enable Mischief"


@dataclass
class PokemonCrystalOptions(PerGameCommonOptions):
    goal: Goal
    johto_only: JohtoOnly
    elite_four_badges: EliteFourBadges
    red_badges: RedBadges
    randomize_badges: RandomizeBadges
    randomize_hidden_items: RandomizeHiddenItems
    require_itemfinder: RequireItemfinder
    trainersanity: Trainersanity
    randomize_pokegear: RandomizePokegear
    randomize_starters: RandomizeStarters
    randomize_wilds: RandomizeWilds
    normalize_encounter_rates: NormalizeEncounterRates
    randomize_static_pokemon: RandomizeStaticPokemon
    randomize_trainer_parties: RandomizeTrainerParties
    randomize_learnsets: RandomizeLearnsets
    tm_compatibility: TMCompatibility
    hm_compatibility: HMCompatibility
    randomize_base_stats: RandomizeBaseStats
    randomize_types: RandomizeTypes
    randomize_palettes: RandomizePalettes
    hm_badge_requirements: HMBadgeRequirements
    reusable_tms: ReusableTMs
    guaranteed_catch: GuaranteedCatch
    minimum_catch_rate: MinimumCatchRate
    blind_trainers: BlindTrainers
    better_marts: BetterMarts
    experience_modifier: ExpModifier
    phone_trap_weight: PhoneTrapWeight
    sleep_trap_weight: SleepTrapWeight
    poison_trap_weight: PoisonTrapWeight
    burn_trap_weight: BurnTrapWeight
    freeze_trap_weight: FreezeTrapWeight
    paralysis_trap_weight: ParalysisTrapWeight
    item_receive_sound: ItemReceiveSound
    enable_mischief: EnableMischief
