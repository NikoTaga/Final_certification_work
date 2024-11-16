import pickle

from numpy import round


def calc_cost(area):
    try:
        area = float(area)
    except:
        area = 0

    model = _load_model("models/rf.pkl")
    scaler_x = _load_model("models/scaler_x.pkl")
    scaler_y = _load_model("models/scaler_y.pkl")

    params = scaler_x.transform([[area]])
    y_pred = model.predict(params)
    result = scaler_y.inverse_transform([y_pred])

    return round(result[0][0], 2)


def _load_model(path):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model




