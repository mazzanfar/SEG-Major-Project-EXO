import React from "react";
import { useSelector } from "react-redux";

function Test() {
    const posts = useSelector((state) => state.posts);
    const size = posts.posts.length;

    return <h1>{size}</h1>;
}

export default Test;
