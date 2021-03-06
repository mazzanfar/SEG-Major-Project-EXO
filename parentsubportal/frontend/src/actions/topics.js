import axios from "axios";

import { GET_TOPICS, ADD_TOPIC } from "./types";

// GET TOPICS
export const getTopics = () => (dispatch) => {
    axios
        .get("/api/topics/")
        .then((res) => {
            dispatch({
                type: GET_TOPICS,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};

export const getTopic = (id) => (dispatch) => {
    axios
        .get("/api/topics/", id)
        .then((res) => {
            dispatch({
                type: GET_TOPIC,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};

// ADD TOPIC
export const addTopic = (topic) => (dispatch) => {
    axios
        .post("/api/topics/", topic)
        .then((res) => {
            dispatch({
                type: ADD_TOPIC,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
