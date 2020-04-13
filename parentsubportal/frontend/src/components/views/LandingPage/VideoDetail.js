import React, { Fragment } from "react";
import { Item, Label } from "semantic-ui-react";
import PostDetail from "./PostDetail";
import YouTube from "react-youtube";

function VideoDetail(props) {
    const opts = {
        height: "460",
        width: "640",
        playersVars: {
            autoplay: 1,
        },
    };
    return (
        <PostDetail post={props.post}>
            <YouTube videoId={props.post.videoId} opts={opts} />
        </PostDetail>
    );
}

export default VideoDetail;
