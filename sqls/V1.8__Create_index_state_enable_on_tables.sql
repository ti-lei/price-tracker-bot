create INDEX  user_sub_good_good_id_price_state_enable_ix ON public.user_sub_good (good_id, price)
    where state = 1;

create INDEX  good_info_state_enable_ix ON public.user_sub_good (good_id)
    where state = 1;

create INDEX  user_state_enable_ix ON public."user" (id,chat_id)
    where state = 1;