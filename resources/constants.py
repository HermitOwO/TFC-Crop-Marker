from typing import Dict, List, Set, NamedTuple, Sequence, Optional, Tuple, Any

class Berry(NamedTuple):
    min_temp: float
    max_temp: float
    min_water: float
    max_water: float
    type: str
    min_forest: str
    max_forest: str

class Crop(NamedTuple):
    type: str
    category: str
    stages: int
    min_temp_wg: float
    max_temp_wg: float
    min_water: float
    max_water: float
    min_temp_growth: float
    max_temp_growth: float
    min_hydration: float
    max_hydration: float
    nitrogen: float
    phosphorous: float
    potassium: float
    min_forest: Optional[int]
    max_forest: Optional[int]

BERRIES: dict[str, Berry] = {
    'blackberry': Berry(-5.2, 19.4, 200, 500, 'spreading', 0, 2),
    'raspberry': Berry(-10.6, 14., 180, 450, 'spreading', 0, 2),
    'blueberry': Berry(-8.8, 8.6, 150, 400, 'spreading', 0, 2),
    'elderberry': Berry(-5.2, 15.8, 120, 380, 'spreading', 0, 2),

    'snowberry': Berry(-10.6, 5, 200, 500, 'stationary', 2, 4),
    'bunchberry': Berry(-14.2, 1.4, 280, 500, 'stationary', 2, 4),
    'gooseberry': Berry(-7, 12.2, 200, 500, 'stationary', 2, 4),
    'cloudberry': Berry(-14.2, 6.8, 80, 320, 'stationary', 2, 4),
    'strawberry': Berry(-1.6, 17.6, 140, 400, 'stationary', 2, 4),
    'wintergreen_berry': Berry(-8.8, 6.8, 100, 370, 'stationary', 2, 4),

    'cranberry': Berry(-14.2, 8.6, 250, 500, 'waterlogged', 2, 4),
}

CROPS: dict[str, Crop] = {
    'cassava': Crop('default', 'legume', 6, 10.4, 40, 260, 500, 10, 47, 45, 100, -50, 40, 20, 3, None),
    'green_bean': Crop('double_stick', 'legume', 8, -4, 19.4, 150, 410, -4, 30, 25, 90, -80, 50, 40, 3, None),
    'lentil': Crop('default', 'legume', 6, -7.6, 19.4, 75, 190, -7, 30, 15, 50, -80, 20, 20, None, None),
    'peanut': Crop('default', 'legume', 6, 12.2, 40, 130, 360, 12, 47, 20, 80, -90, 50, 50, None, None),
    'soybean': Crop('default', 'legume', 7, -9.4, 15.8, 160, 410, -9, 27, 25, 90, -80, 60, 30, 3, None),
    'barley': Crop('default', 'cereal', 8, -9.4, 17.6, 70, 310, -9, 29, 10, 70, 75, -20, -20, None, 2),
    'oat': Crop('default', 'cereal', 8, -9.4, 15.8, 140, 400, -9, 27, 25, 85, 100, -35, -25, None, 2),
    'rye': Crop('default', 'cereal', 8, -9.4, 8.6, 100, 350, -9, 23, 15, 80, 100, -20, -40, None, 2),
    'maize': Crop('double', 'cereal', 6, -9.4, 23., 300, 500, -9, 32, 50, 100, 90, -25, -25, None, 2),
    'wheat': Crop('default', 'cereal', 8, -9.4, 15.8, 100, 400, -9, 27, 15, 85, 100, -30, -30, None, 2),
    'rice': Crop('default', 'cereal', 8, 8.6, 40, 200, 500, 8, 47, 35, 100, 40, 30, 30, 2, None),
    'beet': Crop('default', 'vegetable', 6, -13, 23., 70, 300, -13, 32, 10, 70, 40, 30, 50, None, None),
    'cabbage': Crop('default', 'vegetable', 6, -13, 23., 60, 280, -13, 32, 10, 65, 50, 20, 40, None, None),
    'carrot': Crop('default', 'vegetable', 5, -13, 23., 100, 400, -13, 32, 15, 85, 50, 30, 40, None, None),
    'garlic': Crop('default', 'vegetable', 5, -5.8, 15.8, 60, 310, -5, 27, 10, 70, 40, 20, 50, None, None),
    'onion': Crop('default', 'vegetable', 7, -7.6, 21.2, 100, 390, -7, 31, 15, 85, 40, 40, 40, None, None),
    'potato': Crop('default', 'vegetable', 7, -9.4, 15.8, 200, 420, -9, 27, 35, 90, 40, 20, 60, None, None),
    'squash': Crop('default', 'vegetable', 8, -9.4, 19.4, 90, 390, -9, 30, 15, 85, 25, 45, 50, 3, None),
    'tomato': Crop('double_stick', 'vegetable', 8, 1.4, 40, 120, 390, 1, 47, 20, 85, 30, 40, 50, 3, None),
    'red_bell_pepper': Crop('pickable', 'pickable vegetable', 7, 12.2, 40, 190, 450, 12, 47, 30, 95, 30, 40, 50, None, None),
    'yellow_bell_pepper': Crop('pickable', 'pickable vegetable', 7, 12.2, 40, 190, 450, 12, 47, 30, 95, 30, 40, 50, None, None),
    'pumpkin': Crop('spreading', 'spreading vegetable', 8, -9.4, 23., 120, 390, -9, 32, 20, 85, 40, 30, 60, None, None),
    'melon': Crop('spreading', 'spreading vegetable', 8, 5, 40, 200, 500, 5, 47, 35, 100, 30, 40, 65, None, None),
    'canola': Crop('default', 'cover', 6, -13, 19.4, 120, 320, -35, 17, 20, 75, -30, -60, -100, None, 2),
    'radish': Crop('default', 'cover', 6, -11.2, 23., 190, 410, -33, 21, 30, 90, -50, -100, -60, None, None),
    'alfalfa': Crop('default', 'cover', 6, -9.4, 15.8, 240, 480, -30, 14, 40, 100, -80, -50, -60, None, 2),
    'jute': Crop('double', 'misc', 6, 1.4, 19.4, 100, 410, 1, 30, 15, 90, 60, 40, -40, None, None),
    'papyrus': Crop('double', 'misc', 6, 12.2, 40, 310, 500, 12, 47, 50, 100, 60, -40, 40, None, None),
    'sugarcane': Crop('double', 'misc', 8, 17.6, 40, 160, 500, 17, 47, 25, 100, 50, 50, 50, None, None),
}

STILL_BUSHES = {
    'nightshade': (200, 400, 7, 24),
    'pineapple': (250, 500, 20, 32),
}
