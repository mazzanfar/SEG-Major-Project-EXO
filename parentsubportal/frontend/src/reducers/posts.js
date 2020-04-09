import {
    GET_POSTS,
    GET_POST,
    ADD_POST,
    DELETE_POST,
    DELETE_COMMENT,
    LIKE_POST,
    POST_COMMENT,
} from "../actions/types.js";

const initialState = {
    posts: [],
    post: null,
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
        case DELETE_COMMENT:
            console.log(action.payload);
            return {
                ...state,
                posts: state.posts.map((post) => {
                    if (post.id === action.payload.post) {
                        console.log("hi");
                        return {
                            ...post,
                            total_comments: post.total_comments - 1,
                            comments: post.comments.filter(
                                (comment) => comment.id != action.payload.id
                            ),
                        };
                    }
                    return post;
                }),
            };
        case POST_COMMENT: {
            return {
                ...state,
                total_comments: state.total_comments + 1,
                posts: state.posts.map((post) => {
                    if (post.id === action.payload.post) {
                        return {
                            ...post,
                            total_comments: post.total_comments + 1,
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
