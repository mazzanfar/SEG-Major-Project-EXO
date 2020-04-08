import React, { Fragment, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { Header, Item } from "semantic-ui-react";
import PostDetail from "./LandingPage/PostDetail";
import { useSelector, useDispatch } from "react-redux";
import { getTopics } from "../../actions/topics";
import { getPosts } from "../../actions/posts";

function TopicPage(props) {
    const topics = useSelector((state) => state.topics.topics);
    const posts = useSelector((state) => state.posts.posts);
    const topic = topics.filter(
        (topic) => topic.id == props.match.params.topicId
    )[0];
    const dispatch = useDispatch();
    console.log(topic);

    useEffect(() => {
        dispatch(getTopics());
        dispatch(getPosts(props.match.params.topicId));
    }, [dispatch]);

    return (
        <Fragment>
            <Header>{topic && topic.name}</Header>
            <br />
            {posts &&
                posts.map((post) => (
                    <Item.Group>
                        <PostDetail post={post}></PostDetail>
                    </Item.Group>
                ))}
        </Fragment>
    );
}

export default TopicPage;
