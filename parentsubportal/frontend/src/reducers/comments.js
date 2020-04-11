import { GET_POSTS, POST_COMMENT } from "../actions/types.js";

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
        case POST_COMMENT: {
            console.log("hi");
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
