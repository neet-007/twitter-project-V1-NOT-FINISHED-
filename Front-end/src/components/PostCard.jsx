import React, { useState, useEffect } from 'react'
import ProfilePic from './ProfilePic'
import ProfileCard from './ProfileCard'
import { useNavigate } from 'react-router-dom'
import { Bookmark, Chat, Heart } from 'react-bootstrap-icons'
//import { addLike } from '../data/api'
import { useAddLike } from '../data/queriesAndMutations'
import { useAtom, useSetAtom } from 'jotai'
import { commentDetailsAtom, isCommentAtom } from '../lib/jotai/atoms'


function PostCard({postId, postContent, username, mention, likes, isComment=false}) {

  const navigate = useNavigate()

  const {mutateAsync:addLike, isError} = useAddLike()

  const setCommentDetails = useSetAtom(commentDetailsAtom)
  const setIsComment = useSetAtom(isCommentAtom)

  const switchComment = () => {
    setCommentDetails({
      postIdComment:postId,
      postContentComment:postContent,
      usernameComment:username,
      mentionComment:mention,
      likesComment:likes
    })
  }

  return (
    <article className='post-card-container' onClick={() => {/*switchComment()
                                                             setIsComment(true)
                                                             navigate('/status')*/}}>
        <ProfilePic isHome={true} postCardToProfile={navigate}/>
        <ProfileCard className={'profile-card'} username={username} mention={mention}/>
        <div className='post-content'>
            {postContent}
        </div>
        {isComment ==  false && <img className={'post-img'} src="src/assets/profile-pic.png" alt="" />}
        {isComment ==  true ? <div> replaying to {mention}</div> :
        <div className='post-interact'>
          <span onClick={()=>addLike(postId)}><Heart size={20}/> <span>{likes}</span></span>

          <span onClick={() => {switchComment()
                                setIsComment(true)
                                navigate('/post')}}><Chat size={20}/> <span>0</span></span>

          <span><Bookmark size={20}/> <span>0</span></span>

        </div>
        }
    </article>
  )
}

export default PostCard