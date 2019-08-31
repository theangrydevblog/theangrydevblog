SELECT
  tag_id, name, COUNT(*)
FROM
  theangrydev_tag_posts
LEFT JOIN
  theangrydev_tag
ON
  theangrydev_tag_posts.tag_id = theangrydev_tag.id
GROUP BY
  tag_id, name;
