import axios from "axios";

import { GET_TIMELINE, UPDATE_TIMELINE } from "./types";

// GET DOCUMENTS
export const getTimeline = (childId) => (dispatch) => {
    axios
        .get("/api/timelines/", {
            params: { child: childId },
        })
        .then((res) => {
            dispatch({
                type: GET_TIMELINE,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};

export const updateTimeline = (timeline) => (dispatch) => {
    axios
        .put("/api/timelines/" + timeline.id + "/", timeline)
        .then((res) => {
            dispatch({
                type: UPDATE_TIMELINE,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err.response));
};
