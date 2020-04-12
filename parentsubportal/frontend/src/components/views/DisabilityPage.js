import React, { Fragment, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { Header, Item } from "semantic-ui-react";
import PostDetail from "./LandingPage/PostDetail";
import { useSelector, useDispatch } from "react-redux";
import { getPosts } from "../../actions/posts";
import { getDisabilities } from "../../actions/disabilities";

function DisabilityPage(props) {
    const disabilities = useSelector(
        (state) => state.disabilities.disabilities
    );
    const posts = useSelector((state) => state.posts.posts);
    const disability = disabilities.filter(
        (disability) => disability.id == props.match.params.disabilityId
    )[0];
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getDisabilities());
        dispatch(getPosts({ disability: props.match.params.disabilityId }));
    }, [dispatch]);

    return (
        <Fragment>
            <Header>Viewing by {disability && disability.name}</Header>
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

export default DisabilityPage;
