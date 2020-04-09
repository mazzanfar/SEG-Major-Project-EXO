import { GET_CHILDREN } from "../actions/types";

const initialState = {
    children: [],
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_CHILDREN: {
            return {
                ...state,
                children: action.payload,
            };
        }
        default:
            return state;
    }
}
