import React, { Fragment, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { Header, Item } from "semantic-ui-react";
import PostDetail from "./LandingPage/PostDetail";
import PDFDetail from "./LandingPage/PDFDetail";
import VideoDetail from "./LandingPage/VideoDetail";
import { useSelector, useDispatch } from "react-redux";
import { getTopics } from "../../actions/topics";
import { getResources } from "../../actions/resources";

function TopicPage(props) {
    const topics = useSelector((state) => state.topics.topics);
    const resources = useSelector((state) => state.resources.resources);
    const topic = topics.filter(
        (topic) => topic.id == props.match.params.topicId
    )[0];
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
        dispatch(getResources({ topic: props.match.params.topicId }));
    }, [dispatch]);

    const getItemDetail = (resource) => {
        switch (resource.type) {
            case "pdf":
                return <PDFDetail post={resource.data} />;
            case "post":
                return <PostDetail post={resource.data} />;
            case "video":
                return <VideoDetail post={resource.data} />;
            default:
                return null;
        }
    };

    return (
        <Fragment>
            <Header>Viewing by {topic && topic.name}</Header>
            <p>{topic && topic.description}</p>
            {resources &&
                resources.map((resource) => (
                    <Item.Group>{getItemDetail(resource)}</Item.Group>
                ))}
        </Fragment>
    );
}

export default withRouter(TopicPage);
