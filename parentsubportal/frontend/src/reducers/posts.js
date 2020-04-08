import {
    GET_POSTS,
    GET_POST,
    ADD_POST,
    DELETE_POST,
    LIKE_POST,
    POST_COMMENT,
} from "../actions/types.js";

const initialState = {
    posts: [],
    post: {},
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_POSTS: {
            return {
                ...state,
                posts: action.payload,
            };
        }
        case GET_POST: {
            return {
                ...state,
                post: action.payload,
            };
        }
        case ADD_POST:
            return {
                ...state,
                posts: [action.payload, ...state.posts],
            };
        case DELETE_POST:
            return {
                ...state,
                posts: state.posts.filter((post) => post.id !== action.payload),
            };
        case LIKE_POST:
            return {
                ...state,
                posts: state.posts.map((post) => {
                    if (post.id === action.payload.post) {
                        return {
                            ...post,
                            likes_count: post.likes_count + 1,
                        };
                    }
                    return post;
                }),
            };
        case POST_COMMENT: {
            return {
                ...state,
                posts: state.posts.map((post) => {
                    if (post.id === action.payload.post) {
                        return {
                            ...post,
                            comments: post.comments.concat(action.payload),
                        };
                    }
                    return post;
                }),
            };
        }
        default:
            return state;
    }
}
