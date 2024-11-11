import math

MAX_HISTORY = 24 * 3 + 20

EMOTION_ANGRY = "angry"
EMOTION_DISGUST = "disgust"
EMOTION_FEAR = "fear"
EMOTION_HAPPY = "happy"
EMOTION_NEUTRAL = "neutral"
EMOTION_SAD = "sad"
EMOTION_SURPRISE = "surprise"

def scale_emotion(emotion: str):
    if emotion in EMOTION_ANGRY:
        return 30
    elif emotion in EMOTION_DISGUST:
        return 10
    elif emotion in EMOTION_FEAR:
        return 10
    elif emotion in EMOTION_HAPPY:
        return -30
    elif emotion in EMOTION_NEUTRAL:
        return 0
    elif emotion in EMOTION_SAD:
        return -10
    elif emotion in EMOTION_SURPRISE:
        return -10
    return 0


history = []


def append_history(emotion: str):
    global history
    if len(history) > MAX_HISTORY:
        history = history[1:]
    history.append(emotion.lower())

def get_last_emotion():
    return history[-1]

def calc_score():
    score = 0
    for index in range(len(history)):
        emotion = history[index]
        score = max(score + scale_emotion(emotion) * decrease_factor(index), 0)
    return score

def decrease_factor(index):
    global history
    x = (len(history) - 1 - index) / len(history)
    a = 1.2
    return math.sqrt(1 - x**2 / a)
