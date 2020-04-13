import React, { Fragment, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Item, Label } from "semantic-ui-react";
import VideoDetail from "./VideoDetail";
import { getVideos } from "../../../actions/videos";
import YouTube from "react-youtube";
import Comments from "./Comments";

function VideoPosts() {
    const dispatch = useDispatch();
    const videos = useSelector((state) => state.videos.videos);
    const opts = {
        height: "460",
        width: "640",
        playersVars: {
            autoplay: 1,
        },
    };

    useEffect(() => {
        dispatch(getVideos());
    }, [dispatch]);

    return (
        <Fragment>
            <br />
            {videos.map((video) => (
                <Item.Group>
                    <VideoDetail post={video} />
                </Item.Group>
            ))}
        </Fragment>
    );
}

export default VideoPosts;
