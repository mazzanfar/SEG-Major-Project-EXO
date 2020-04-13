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
    const sortedResources = resources.filter((resource) =>
        resource.data.topics.includes(topic.id)
    );
    console.log(sortedResources);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
        dispatch(getResources({ topics: props.match.params.topicId }));
    }, [dispatch]);

    const getItemDetail = (resource) => {
        switch (resource.type) {
            case "pdf":
                return (
                    <Fragment>
                        <h3>PDF</h3>
                        <PDFDetail post={resource.data} />
                    </Fragment>
                );
            case "post":
                return (
                    <Fragment>
                        <h3>Post</h3>
                        <PostDetail post={resource.data} />
                    </Fragment>
                );
            case "video":
                return (
                    <Fragment>
                        <h3>Video</h3>
                        <VideoDetail post={resource.data} />
                    </Fragment>
                );
            default:
                return null;
        }
    };

    return (
        <Fragment>
            <Header>Viewing by {topic && topic.name}</Header>
            {resources &&
                sortedResources.map((resource) => (
                    <Item.Group>{getItemDetail(resource)}</Item.Group>
                ))}
        </Fragment>
    );
}

export default withRouter(TopicPage);
