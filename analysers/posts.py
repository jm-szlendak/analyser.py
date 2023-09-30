import dateutil.parser as dateutil
import datetime

POST_TYPE_QUESTION = '1'
POST_TYPE_ANSWER = '2'
DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

def analyse_posts(xmlIterator):
    total_posts = 0
    total_accepted_posts = 0
    avg_score = 0
    first_post_created_date = datetime.datetime(2030, 1, 1, 0, 0)
    last_post_created_date = datetime.datetime(1970, 1, 1, 0, 0)
    score_sum = 0


    for _, element in xmlIterator:
        if (element.tag == 'row'):
            data = element.attrib
            total_posts += 1
            if 'Score' in data:
                score_sum += int(data['Score'])

            if 'AcceptedAnswerId' in data:
                total_accepted_posts += 1

            created_date = dateutil.parse(data['CreationDate'])
            if (created_date > last_post_created_date):
                last_post_created_date = created_date

            if (created_date < first_post_created_date):
                first_post_created_date = created_date

        element.clear()

    avg_score = score_sum / total_posts

    return {
        'total_posts_count': total_posts,
        'total_answered_posts_count': total_accepted_posts,
        'avg_response_score': avg_score,
        'oldest_post_create_date': first_post_created_date.strftime(DATE_FORMAT),
        'newest_post_create_date': last_post_created_date.strftime(DATE_FORMAT),
    }