import React, { Fragment, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { Header, Item } from "semantic-ui-react";
import PostDetail from "./LandingPage/PostDetail";
import { useSelector, useDispatch } from "react-redux";
import { getTopics } from "../../actions/topics";
import { getPosts } from "../../actions/posts";
import { getResources } from "../../actions/resources";

function TopicPage(props) {
    const isFetching = useSelector((state) => state);
    const topics = useSelector((state) => state.topics.topics);
    const resources = useSelector((state) => state.resources.resources);
    console.log(resources);
    const topic = topics.filter(
        (topic) => topic.id == props.match.params.topicId
    )[0];
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
        dispatch(getResources({ topic: props.match.params.topicId }));
    }, [dispatch]);

    return (
        <Fragment>
            {isFetching ? (
                <Header>Loading...</Header>
            ) : (
                <Header>Viewing by {topic && topic.name}</Header>
            )}
        </Fragment>
    );
}

export default TopicPage;
