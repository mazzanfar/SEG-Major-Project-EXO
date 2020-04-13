import { GET_TIMELINE } from "../actions/types.js";

const initialState = {
    timeline: null,
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_TIMELINE: {
            return {
                ...state,
                timeline: action.payload,
            };
        }
        default:
            return state;
    }
}
