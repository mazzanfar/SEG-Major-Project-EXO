import axios from "axios";

import { RATE_POST, UPDATE_RATING } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// GET POSTS
export const ratePost = (rating) => (dispatch) => {
    axios
        .post("/api/ratings/", rating)
        .then((res) => {
            dispatch({
                type: RATE_POST,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err.message));
};

export const updateRating = (rating) => (dispatch) => {
    console.log(rating);
    axios
        .put("/api/ratings/" + rating.id + "/", rating)
        .then((res) => {
            dispatch({
                type: UPDATE_RATING,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err.response));
};
