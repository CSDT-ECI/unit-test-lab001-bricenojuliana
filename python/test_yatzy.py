from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance_scores_sum_of_all_dice():
        #Arrange
        dice = [1, 1, 3, 3, 6]
        #Act
        result = Yatzy.chance(*dice)
        #Assert
        assert result == 14

def test_yatzy_scores_50_if_all_dice_same():
        #Arrange
        dice = [1, 1, 1, 1, 1]
        #Act
        result = Yatzy.yatzy(dice)
        #Assert
        assert result == 50

def test_yatzy_scores_0_if_not_all_dice_same():
        #Arrange
        dice = [1, 1, 1, 2, 1]
        #Act
        result = Yatzy.yatzy(dice)
        #Assert
        assert result == 0

def test_ones_score_sum_of_ones():
        #Arrange
        dice = [1, 1, 2, 4, 4]
        #Act
        result = Yatzy.ones(*dice)
        #Assert
        assert result == 2

def test_ones_score_0_if_no_ones():
        #Arrange
        dice = [2, 3, 4, 5, 6]
        #Act
        result = Yatzy.ones(*dice)
        #Assert
        assert result == 0

def test_twos_score_sum_of_twos():
        #Arrange
        dice = [2, 3, 2, 5, 1]
        #Act
        result = Yatzy.twos(*dice)
        #Assert
        assert result == 4

def test_twos_score_0_if_no_twos():
        #Arrange
        dice = [1, 3, 4, 5, 6]
        #Act
        result = Yatzy.twos(*dice)
        #Assert
        assert result == 0

def test_threes_score_sum_of_threes():
        #Arrange
        dice = [3, 3, 3, 4, 5]
        #Act
        result = Yatzy.threes(*dice)
        #Assert
        assert result == 9

def test_threes_score_0_if_no_threes():
        #Arrange
        dice = [1, 2, 4, 5, 6]
        #Act
        result = Yatzy.threes(*dice)
        #Assert
        assert result == 0

def test_fours_score_sum_of_fours():
        #Arrange
        dice = [4, 4, 4, 5, 5]
        #Act
        yatzy = Yatzy(*dice)
        result = yatzy.fours()
        #Assert
        assert result == 12

def test_fours_score_0_if_no_fours():
        #Arrange
        dice = [1, 2, 3, 5, 6]
        #Act
        yatzy = Yatzy(*dice)
        result = yatzy.fours()
        #Assert
        assert result == 0

def test_fives_score_sum_of_fives():
        #Arrange
        dice = [5, 4, 5, 5, 3]
        #Act
        yatzy = Yatzy(*dice)
        result = yatzy.fives()
        #Assert
        assert result == 15

def test_fives_score_0_if_no_fives():
        #Arrange
        dice = [1, 2, 3, 4, 6]
        #Act
        yatzy = Yatzy(*dice)
        result = yatzy.fives()
        #Assert
        assert result == 0

def test_sixes_score_sum_of_sixes():
        #Arrange
        dice = [6, 5, 2, 6, 1]
        #Act
        yatzy = Yatzy(*dice)
        result = yatzy.sixes()
        #Assert
        assert result == 12

def test_sixes_score_0_if_no_sixes():
        #Arrange
        dice = [1, 2, 3, 4, 5]
        #Act
        yatzy = Yatzy(*dice)
        result = yatzy.sixes()
        #Assert
        assert result == 0

def test_one_pair_scores_sum_of_2_dice_in_HIGHEST_PAIR():
        #Arrange
        dice = [3, 5, 3, 5, 6]
        #Act
        result = Yatzy.score_pair(*dice)
        #Assert
        assert result == 10

def test_one_pair_scores_0_if_no_PAIRS():
        #Arrange
        dice = [1, 2, 3, 4, 5]
        #Act
        result = Yatzy.score_pair(*dice)
        #Assert
        assert result == 0

def test_two_Pair_scores_sum_of_4_dice_in_2_PAIRS():
        #Arrange
        dice = [3, 3, 5, 4, 5]
        #Act
        result = Yatzy.two_pair(*dice)
        #Assert
        assert result == 16

def test_two_Pair_scores_0_if_no_2_PAIRS():
        #Arrange
        dice = [3, 3, 1, 4, 5]
        #Act
        result = Yatzy.two_pair(*dice)
        #Assert
        assert result == 0

def test_three_of_a_kind_scores_sum_of_3_DICE():
        #Arrange
        dice = [3, 3, 3, 4, 5]
        #Act
        result = Yatzy.three_of_a_kind(*dice)
        #Assert
        assert result == 9

def test_three_of_a_kind_scores_0_if_no_THREE_OF_A_KIND():
        #Arrange
        dice = [3, 3, 4, 5, 6]
        #Act
        result = Yatzy.three_of_a_kind(*dice)
        #Assert
        assert result == 0

def test_four_of_a_kinds_scores_sum_of_4_DICE():
        #Arrange
        dice = [2, 2, 2, 2, 5]
        #Act
        result = Yatzy.four_of_a_kind(*dice)
        #Assert
        assert result == 8

def test_four_of_a_kinds_scores_0_if_no_FOUR_OF_A_KIND():
        #Arrange
        dice = [2, 2, 2, 5, 5]
        #Act
        result = Yatzy.four_of_a_kind(*dice)
        #Assert
        assert result == 0

def test_small_straight_scores_15():
        #Arrange
        dice = [1, 2, 3, 4, 5]
        #Act
        result = Yatzy.smallStraight(*dice)
        #Assert
        assert result == 15

def test_small_straight_scores_0_if_not_a_SMALL_STRAIGHT():
        #Arrange
        dice = [1, 2, 2, 4, 5]
        #Act
        result = Yatzy.smallStraight(*dice)
        #Assert
        assert result == 0

def test_large_straight_scores_20():
        #Arrange
        dice = [2, 3, 4, 5, 6]
        #Act
        result = Yatzy.largeStraight(*dice)
        #Assert
        assert result == 20

def test_large_straight_scores_0_if_not_a_LARGE_STRAIGHT():
        #Arrange
        dice = [1, 2, 3, 4, 5]
        #Act
        result = Yatzy.largeStraight(*dice)
        #Assert
        assert result == 0

def test_full_house_scores_sum_of_all_DICE():
        #Arrange
        dice = [6, 2, 2, 2, 6]
        #Act
        result = Yatzy.fullHouse(*dice)
        #Assert
        assert result == 18

def test_full_house_scores_0_if_not_a_full_HOUSE():
        #Arrange
        dice = [2, 3, 4, 5, 6]
        #Act
        result = Yatzy.fullHouse(*dice)
        #Assert
        assert result == 0

