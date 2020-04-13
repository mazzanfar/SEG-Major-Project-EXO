import React, { Component, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getVideo } from "../../actions/videos";
import VideoDetail from "./LandingPage/VideoDetail";
import { Item } from "semantic-ui-react";

function VideoPage(props) {
    const videoId = props.match.params.videoId;
    const post = useSelector((state) => state.videos.video);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getVideo(videoId));
    }, [dispatch]);

    return post ? (
        <Item.Group>
            <VideoDetail post={post} />
        </Item.Group>
    ) : null;
}
export default VideoPage;
