import { GET_DISABILITIES } from "../actions/types.js";

const initialState = {
    disabilities: [],
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_DISABILITIES: {
            return {
                ...state,
                disabilities: action.payload,
            };
        }
        default:
            return state;
    }
}
